import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    padding: 5,
  },
  detail: {
    flexDirection: 'row',
    alignItems: 'center',
    marginRight: 5,
    padding: 2,
  },
  detail_emoji: {
    fontSize: 21,
    marginRight: 3,
  },
  detail_like: {
    fontSize: 14,
    fontWeight: 'bold',
  },
  no_socials: {
    fontSize: 16,
    fontWeight: 'bold',
    padding: 3,
  },
});

export default styles;
