import React from 'react';
import { Button, View, Text } from 'react-native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import { FoodtruckDetailsPage, ProductDetailsPage } from '../pages';

const Stack = createNativeStackNavigator();

const Home = ({ navigation }) => {
  return (
    <View>
      <Text>Dummy Home Screen</Text>

      <Button
        title="Go to Chicken Taco"
        onPress={() => {
          navigation.push('Product Details', {
            slug: 'chicken-taco',
          });
        }}
      />
      <Button
        title="Go to Taco Truck"
        onPress={() => {
          navigation.push('Foodtruck Details', {
            slug: 'taco-truck',
          });
        }}
      />
    </View>
  );
};

const AppRouter = () => (
  <Stack.Navigator initialRouteName="Home">
    <Stack.Screen name="Home" component={Home} />

    <Stack.Screen name="Foodtruck Details" component={FoodtruckDetailsPage} />

    <Stack.Screen name="Product Details" component={ProductDetailsPage} />
  </Stack.Navigator>
);

export default AppRouter;
