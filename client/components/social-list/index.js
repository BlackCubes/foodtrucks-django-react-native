import React from 'react';
import { Text, View } from 'react-native';

const SocialList = ({ socials }) => {
  if (!socials.length) return <Text>No Socials!</Text>;

  return socials.map((social) => (
    <View key={social.uuid}>
      <Text>
        {social.emoji} {social.like}
      </Text>
    </View>
  ));
};

export default SocialList;
