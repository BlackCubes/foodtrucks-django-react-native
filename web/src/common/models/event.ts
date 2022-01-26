import { NestedFoodtruck } from './foodtruck';

export interface Event {
  uuid: string;
  date: string;
  start_time: string;
  end_time: string;
  truck: NestedFoodtruck[] | [];
}
