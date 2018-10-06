import axios from 'axios';
import {
  FETCH_TASKS_START,
  FETCH_TASKS_SUCCESS,
  FETCH_TASKS_FAILURE,
  SHOW_CREATE_FORM
} from '../actionTypes';

const backend = 'https://api.taschengeldboerse.io';

function Sleep(milliseconds) {
  return new Promise(resolve => setTimeout(resolve, milliseconds));
}

export const showCreateForm = () => ({ type: SHOW_CREATE_FORM });

export const fetchTasks = () => async dispatch => {
  try {
    dispatch({ type: FETCH_TASKS_START });

    const res = await axios.get(`${backend}/tasks`);
    const extractDataOrEmptyArray = (response) => (response.data) || [];

    await Sleep(500);

    dispatch({ type: FETCH_TASKS_SUCCESS, payload: extractDataOrEmptyArray(res) });
  } catch (error) {
    dispatch({ type: FETCH_TASKS_FAILURE, payload: false });
  }
};

export const submitTask = () => async dispatch => {
  try {
    dispatch({ type: FETCH_TASKS_START });

    const res = await axios.get(`${backend}/tasks`);
    const extractDataOrEmptyArray = (response) => (response.data) || [];

    await Sleep(500);

    dispatch({ type: FETCH_TASKS_SUCCESS, payload: extractDataOrEmptyArray(res) });
  } catch (error) {
    dispatch({ type: FETCH_TASKS_FAILURE, payload: false });
  }
};
