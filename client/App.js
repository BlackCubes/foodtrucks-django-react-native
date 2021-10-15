import React from 'react';
import { Provider } from 'react-redux';
import { NavigationContainer } from '@react-navigation/native';

import { store } from './old-redux/store';
import AppRouter from './router';

export default function App() {
  return (
    <Provider store={store}>
      <NavigationContainer>
        <AppRouter />
      </NavigationContainer>
    </Provider>
  );
}
