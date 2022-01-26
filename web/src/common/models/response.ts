type MetaData = {
  total_count: number;
  next: null | string;
  previous: null | string;
};

export interface SuccessResponse {
  status: string;
  status_code: number;
  meta_data: MetaData;
}
