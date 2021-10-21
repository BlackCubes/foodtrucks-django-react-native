import React from 'react';
import { Button, Text, View } from 'react-native';

const EmojiList = ({ addSocial, emojis, productSlug }) => {
  if (!emojis.length) return <Text>No emojis!</Text>;

  return emojis.map((emoji) => (
    <View key={emoji.uuid}>
      <Button
        title={emoji.emoji}
        onPress={() => addSocial(emoji.emoji, productSlug, 1)}
      />
    </View>
  ));
};

export default EmojiList;
