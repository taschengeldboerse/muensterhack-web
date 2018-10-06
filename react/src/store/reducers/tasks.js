import { combineReducers } from 'redux'
import {
  FETCH_TASKS_START,
  FETCH_TASKS_SUCCESS,
  FETCH_TASKS_FAILURE
} from '../actionTypes';

const list = (state = [], action) => {
  switch (action.type) {
    case FETCH_TASKS_SUCCESS:
      return action.payload;
    default:
      return state;
  }
};

const isLoading = (state = false, action) => {
  switch (action.type) {
    case FETCH_TASKS_START:
      return true;
    case FETCH_TASKS_SUCCESS:
    case FETCH_TASKS_FAILURE:
      return false;
    default:
      return state;
  }
};

const hasError = (state = false, action) => {
  switch (action.type) {
    case FETCH_TASKS_FAILURE:
      return true;
    case FETCH_TASKS_START:
    case FETCH_TASKS_SUCCESS:
      return false;
    default:
      return state;
  }
};

export default combineReducers({ isLoading, list, hasError })