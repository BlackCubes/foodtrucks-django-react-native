import React, { useRef } from 'react';
import { Animated, Pressable, Text, View } from 'react-native';

import styles from './styles';

const EmojiList = ({ addSocial, emojis, productSlug }) => {
  const onPressedIn = (scaling, translation) => {
    Animated.timing(scaling, {
      toValue: 1.2,
      duration: 50,
      useNativeDriver: true,
    }).start();

    Animated.timing(translation, {
      toValue: -7,
      duration: 50,
      useNativeDriver: true,
    }).start();
  };

  const onPressedOut = (scaling, translation) => {
    Animated.timing(scaling, {
      toValue: 1,
      duration: 50,
      useNativeDriver: true,
    }).start();

    Animated.timing(translation, {
      toValue: 0,
      duration: 50,
      useNativeDriver: true,
    }).start();
  };

  if (!emojis.length) return <Text>No emojis!</Text>;

  return (
    <View style={styles.container}>
      {emojis.map((emoji) => {
        const scaling = useRef(new Animated.Value(1)).current;
        const translation = useRef(new Animated.Value(0)).current;

        return (
          <View key={emoji.uuid} style={styles.emoji_wrapper}>
            <Pressable
              onPressIn={() => onPressedIn(scaling, translation)}
              onPressOut={() => onPressedOut(scaling, translation)}
              onPress={() => addSocial(emoji.emoji, productSlug, 1)}
            >
              <Animated.Text
                style={{
                  ...styles.emoji,
                  transform: [{ translateY: translation }, { scale: scaling }],
                }}
              >
                {emoji.emoji}
              </Animated.Text>
            </Pressable>
          </View>
        );
      })}
    </View>
  );
};

export default EmojiList;
