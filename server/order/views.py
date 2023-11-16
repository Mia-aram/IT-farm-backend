from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import Order, Review
from .serializers import *
from farms.distance import geocoding, distance

# 주문하기 
class OrderCreateView(APIView):
    def post(self, request):
        user_id = request.member.get('id')
        address = request.data.get('address')
        latitude, longitude = geocoding(address)
        center = distance(latitude,longitude)
        serializer = OrderSerializer(data={**request.data, 'user_id':user_id, 'center':center})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# 주문삭제
class OrderDeleteView(APIView):
    def delete(self, request, order_id):
        # pk = request.data.get('order_id')
        order = get_object_or_404(Order, order_id=order_id)
        try:
            order.delete()
            return Response({'message': '삭제'}, status=status.HTTP_200_OK)
        except:
            return Response({'message': '실패'}, status=status.HTTP_400_BAD_REQUEST)

class OrderReadView(APIView):
    def get(self, request):
        # pk = request.data.get('order_id')
        user_id = request.member.get('id')
        order = Order.objects.filter(user_id=user_id)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# # 결제하기
# class OrderPayView(APIView):
#     def get(self, request, order_id):
#         # pk = request.data.get('order_id')
#         order = Order.objects.get(order_id=order_id)
        
#         # 결제 완료되면 0 -> 1 변경 
#         if order:
#             order.status = 1
#             order.save()
#             return Response({'message': '성공'}, status=status.HTTP_200_OK)        
#         return Response({'message': '실패'}, status=status.HTTP_400_BAD_REQUEST)
    
# 리뷰쓰기
class ReviewCreateView(APIView):
    def post(self, request):
        pk = request.data.get('order_id')

        # 결제 완료 된 주문만
        order = Order.objects.get(order_id=pk)
        try:
            if order.status == 0:
                review_data = {
                    'order': order.order_id,
                    'nickname': order.nickname, 
                    'product_id': order.product.id,
                    'content': request.data.get('content'),
                    'score': request.data.get('score'),
                    'photo': request.data.get('photo', None),
                    'kind': order.product.kind
                }
            else:
                return Response({'message':'이미 리뷰 등록'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': '주문번호가 존재하지 않음'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = ReviewSerializer(data=review_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 리뷰 수정
class ReviewUpdateView(APIView):
    def post(self, request):
        pk = request.data.get('review_id')
        reviews = get_object_or_404(Review, review_id=pk)
        serializer = ReviewUPdateSerializer(reviews, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# 리뷰 삭제
class ReviewDeleteView(APIView):
    def delete(self, request, review_id):
        # pk = request.data.get('review_id')
        review = get_object_or_404(Review, review_id=review_id)
        try:
            review.delete()
            return Response({'message': '삭제'}, status=status.HTTP_200_OK)
        except:
            return Response({'message': '삭제 실패'}, status=status.HTTP_400_BAD_REQUEST)
        
class ReviewReadView(APIView):
    def get(self, request, product_id):
        reviews = Review.objects.filter(product_id=product_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
