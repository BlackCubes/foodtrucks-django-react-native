import React, { useEffect, useLayoutEffect } from 'react';
import { Button, FlatList, Text, View } from 'react-native';
import { connect } from 'react-redux';

import { EmojiList, SocialList } from '../../components';

import { retrieveOneProduct } from '../../old-redux/actions/productActions';
import {
  addReview,
  retrieveAllReviewsFromProduct,
} from '../../old-redux/actions/reviewActions';
import {
  addSocial,
  retrieveAllEmojis,
  retrieveAllSocialsFromProduct,
} from '../../old-redux/actions/socialActions';

const mapStateToProps = (state) => ({
  emojis: state.social.emojis,
  product: state.product.product,
  productReviews: state.review.productReviews,
  productSocials: state.social.productSocials,
});

const mapDispatchToProps = (dispatch) => ({
  commenceAddReview: (review, product_slug, user_uuid) =>
    dispatch(addReview(review, product_slug, user_uuid)),
  commenceAddSocial: (emoji, product_slug, like) =>
    dispatch(addSocial(emoji, product_slug, like)),
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
  commenceAddSocial,
  commenceRetrieveAllEmojis,
  commenceRetrieveAllReviewsFromProduct,
  commenceRetrieveAllSocialsFromProduct,
  commenceRetrieveOneProduct,
  emojis,
  navigation,
  product,
  productReviews,
  productSocials,
  route,
}) => {
  const { slug } = route.params;

  useLayoutEffect(() => {
    navigation.setOptions({
      title: !product ? 'Product' : `Product: ${product.name}`,
    });
  }, [navigation, product]);

  useEffect(() => {
    if (slug) {
      commenceRetrieveAllEmojis();
      commenceRetrieveOneProduct(slug);
      commenceRetrieveAllSocialsFromProduct(slug);
      commenceRetrieveAllReviewsFromProduct(slug);
    }
  }, [slug]);

  if (!product) return <Text>No products</Text>;

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

      <SocialList socials={productSocials} />

      <EmojiList
        addSocial={commenceAddSocial}
        emojis={emojis}
        productSlug={slug}
      />

      <View
        style={{
          borderBottomColor: 'black',
          borderBottomWidth: 1,
        }}
      />

      <FlatList
        data={productReviews}
        keyExtractor={(item) => item.uuid}
        ListEmptyComponent={() => <Text>No reviews</Text>}
        renderItem={({ item }) => (
          <View>
            <Text>
              Created by {item.user} at {item.created_at}
            </Text>

            <Text>Review: {item.review}</Text>
          </View>
        )}
      />
    </View>
  );
};

export default connect(mapStateToProps, mapDispatchToProps)(ProductDetailsPage);
