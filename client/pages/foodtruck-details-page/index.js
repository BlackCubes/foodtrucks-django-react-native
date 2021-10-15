import React, { useEffect, useLayoutEffect } from 'react';
import { Button, FlatList, Text, View } from 'react-native';
import { connect } from 'react-redux';

import { retrieveOneFoodtruck } from '../../old-redux/actions/foodtruckActions';
import { retrieveAllProductsFromFoodtruck } from '../../old-redux/actions/productActions';
import { retrieveAllReviewsFromFoodtruck } from '../../old-redux/actions/reviewActions';
import {
  addSocial,
  retrieveAllEmojis,
  retrieveAllSocialsFromFoodtruck,
} from '../../old-redux/actions/socialActions';

const mapStateToProps = (state) => ({
  emojis: state.social.emojis,
  foodtruck: state.foodtruck.foodtruck,
  foodtruckReviews: state.review.foodtruckReviews,
  foodtruckSocials: state.social.foodtruckSocials,
});

const mapDispatchToProps = (dispatch) => ({
  commenceAddSocial: (emoji, product_slug, like) =>
    dispatch(addSocial(emoji, product_slug, like)),
  commenceRetrieveAllEmojis: () => dispatch(retrieveAllEmojis()),
  commenceRetrieveAllProductsFromFoodtruck: (foodtruck_slug) =>
    dispatch(retrieveAllProductsFromFoodtruck(foodtruck_slug)),
  commenceRetrieveAllReviewsFromFoodtruck: (foodtruck_slug) =>
    dispatch(retrieveAllReviewsFromFoodtruck(foodtruck_slug)),
  commenceRetrieveAllSocialsFromFoodtruck: (foodtruck_slug) =>
    dispatch(retrieveAllSocialsFromFoodtruck(foodtruck_slug)),
  commenceRetrieveOneFoodtruck: (foodtruck_slug) =>
    dispatch(retrieveOneFoodtruck(foodtruck_slug)),
});

const FoodtruckDetailsPage = ({
  commenceAddSocial,
  commenceRetrieveAllEmojis,
  commenceRetrieveAllProductsFromFoodtruck,
  commenceRetrieveAllReviewsFromFoodtruck,
  commenceRetrieveAllSocialsFromFoodtruck,
  commenceRetrieveOneFoodtruck,
  emojis,
  foodtruck,
  foodtruckReviews,
  foodtruckSocials,
  navigation,
  route,
}) => {
  const { slug } = route.params;

  useLayoutEffect(() => {
    navigation.setOptions({
      title: !foodtruck ? 'Foodtruck' : `Foodtruck: ${foodtruck.name}`,
    });
  }, [navigation, foodtruck]);

  useEffect(() => {
    if (slug) {
      commenceRetrieveAllEmojis();
      commenceRetrieveOneFoodtruck(slug);
      commenceRetrieveAllProductsFromFoodtruck(slug);
      commenceRetrieveAllSocialsFromFoodtruck(slug);
      commenceRetrieveAllReviewsFromFoodtruck(slug);
    }
  }, [slug]);

  if (!foodtruck) return <Text>No foodtruck!</Text>;

  return (
    <View>
      <Text>Foodtruck: {foodtruck.name}</Text>

      <Text>Info: {foodtruck.info}</Text>

      <Text>Phone Number: {foodtruck.phone_number}</Text>

      <Text>Email: {foodtruck.email}</Text>

      <Text>Website: {foodtruck.website}</Text>

      <View
        style={{
          borderBottomColor: 'black',
          borderBottomWidth: 1,
        }}
      />

      <FlatList
        data={foodtruckSocials}
        keyExtractor={(item) => item.uuid}
        ListEmptyComponent={() => <Text>No Socials!</Text>}
        renderItem={({ item }) => (
          <View>
            <Text>
              {item.emoji} {item.like}
            </Text>
          </View>
        )}
      />

      <FlatList
        data={emojis}
        keyExtractor={(item) => item.uuid}
        ListEmptyComponent={() => <Text>No Emojis!</Text>}
        renderItem={({ item }) => (
          <Button
            title={item.emoji}
            onPress={() => commenceAddSocial(item.emoji, slug, 1)}
          />
        )}
      />

      <View
        style={{
          borderBottomColor: 'black',
          borderBottomWidth: 1,
        }}
      />

      <FlatList
        data={foodtruckReviews}
        keyExtractor={(item) => item.uuid}
        ListEmptyComponent={() => <Text>No Reviews!</Text>}
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

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(FoodtruckDetailsPage);
