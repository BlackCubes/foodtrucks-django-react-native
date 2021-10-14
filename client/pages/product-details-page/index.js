import React, { useEffect } from 'react';
import { FlatList, Text, View } from 'react-native';
import { connect } from 'react-redux';
import { useParams } from 'react-router-native';

import { retrieveOneProduct } from '../../old-redux/actions/productActions';
import {
  addReview,
  retrieveAllReviewsFromProduct,
} from '../../old-redux/actions/reviewActions';
import {
  retrieveAllEmojis,
  retrieveAllSocialsFromProduct,
} from '../../old-redux/actions/socialActions';

const mapStateToProps = (state) => ({
  emojis: state.socials.emojis,
  product: state.product.product,
  productReviews: state.review.productReviews,
  productSocials: state.social.productSocials,
});

const mapDispatchToProps = (dispatch) => ({
  commenceAddReview: (review, product_slug, user_uuid) =>
    dispatch(addReview(review, product_slug, user_uuid)),
  commenceRetrieveAllEmojis: () => dispatch(retrieveAllEmojis()),
  commenceRetrieveAllReviewsFromProduct: (product_slug) =>
    dispatch(retrieveAllReviewsFromProduct(product_slug)),
  commenceRetrieveAllSocialsFromProduct: (product_slug) =>
    dispatch(retrieveAllSocialsFromProduct(product_slug)),
  commenceRetrieveOneProduct: (product_slug) =>
    dispatch(retrieveOneProduct(product_slug)),
});

const ProductDetailsPage = ({
  commenceAddReview,
  commenceRetrieveAllEmojis,
  commenceRetrieveAllReviewsFromProduct,
  commenceRetrieveAllSocialsFromProduct,
  commenceRetrieveOneProduct,
  emojis,
  product,
  productReviews,
  productSocials,
}) => {
  const { slug } = useParams();

  useEffect(() => {
    if (slug) {
      commenceRetrieveAllEmojis();
      commenceRetrieveOneProduct(slug);
      commenceRetrieveAllSocialsFromProduct(slug);
      commenceRetrieveAllReviewsFromProduct(slug);
    }
  }, [slug]);

  if (!product) return <Text>No products</Text>;

  console.log(productSocials);

  return (
    <View>
      <Text>Product: {product.name}</Text>

      <Text>Info: {product.info}</Text>

      <Text>Price: {product.price}</Text>

      <Text>Quantity: {product.quantity}</Text>

      <Text>Foodtruck: {product.truck}</Text>

      <View
        style={{
          borderBottomColor: 'black',
          borderBottomWidth: 1,
        }}
      />

      <FlatList
        data={emojis}
        keyExtractor={(emoji) => emoji.uuid}
        ListEmptyComponent={() => <Text>No emojis!</Text>}
        renderItem={({ emoji }) => (
          <View>
            <Text>{emoji}</Text>
          </View>
        )}
      />

      <View
        style={{
          borderBottomColor: 'black',
          borderBottomWidth: 1,
        }}
      />

      <FlatList
        data={productReviews}
        keyExtractor={(review) => review.uuid}
        ListEmptyComponent={() => <Text>No reviews</Text>}
        renderItem={({ review, user, created_at }) => (
          <View>
            <Text>
              Created by {user} at {created_at}
            </Text>

            <Text>Review: {review}</Text>
          </View>
        )}
      />
    </View>
  );
};

export default connect(mapStateToProps, mapDispatchToProps)(ProductDetailsPage);
