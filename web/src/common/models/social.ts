import { NestedProduct } from './product';

export interface Emoji {
  uuid: string;
  emoji: string;
  name: string;
}

export interface Social {
  uuid: string;
  like: number;
  emoji: Emoji;
  product: Pick<NestedProduct, 'uuid' | 'name' | 'slug'>;
}
