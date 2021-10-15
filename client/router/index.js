import React from 'react';
import { View, Text } from 'react-native';
import { Link, NativeRouter, Route, Switch } from 'react-router-native';

import { ProductDetailsPage } from '../pages';

const AppRouter = () => (
  <NativeRouter>
    <View>
      <Link to="/products/chicken-taco">
        <Text>Chicken Taco</Text>
      </Link>

      <Switch>
        <Route path="/products/:slug" exact component={ProductDetailsPage} />
      </Switch>
    </View>
  </NativeRouter>
);

export default AppRouter;
