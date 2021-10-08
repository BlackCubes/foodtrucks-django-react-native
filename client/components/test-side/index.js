import React, { useEffect } from "react";
import { Text } from "react-native";
import { connect } from "react-redux";

import { allFoodtrucks } from "../../old-redux/actions/foodtruckActions";

const mapStateToProps = (state) => ({
  foodtrucks: state.foodtruck.foodtrucks,
});

const mapDispatchToProps = (dispatch) => ({
  commenceAllFoodtrucks: () => dispatch(allFoodtrucks()),
});

const TestComponent = ({ commenceAllFoodtrucks, foodtrucks }) => {
  console.log("Foodtrucks: ", foodtrucks);

  useEffect(() => commenceAllFoodtrucks(), []);

  return <Text>This is a test component</Text>;
};

export default TestComponent;
