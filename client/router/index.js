import React from 'react';
import { Button, View, Text } from 'react-native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import { ProductDetailsPage } from '../pages';

const Stack = createNativeStackNavigator();

const Home = ({ navigation }) => {
  return (
    <View>
      <Text>Dummy Home Screen</Text>

      <Button
        title="Go to Chicken Taco"
        onPress={() => {
          navigation.push('ProductDetails', {
            slug: 'chicken-taco',
          });
        }}
      />
    </View>
  );
};

const AppRouter = () => (
  <Stack.Navigator initialRouteName="Home">
    <Stack.Screen name="Home" component={Home} />

    <Stack.Screen name="ProductDetails" component={ProductDetailsPage} />
  </Stack.Navigator>
);

export default AppRouter;
