import React from 'react';
import { Text, View } from 'react-native';

import styles from './styles';

const SocialList = ({ socials }) => {
  if (!socials.length)
    return (
      <View style={styles.container}>
        <Text style={styles.no_socials}>No socials!</Text>
      </View>
    );

  return (
    <View style={styles.container}>
      {socials.map((social) => (
        <View key={social.uuid} style={styles.detail}>
          <Text style={styles.detail_emoji}>{social.emoji}</Text>

          <Text style={styles.detail_like}>{social.like}</Text>
        </View>
      ))}
    </View>
  );
};

export default SocialList;
