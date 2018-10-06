import axios from 'axios';
import {
  FETCH_TASKS_START,
  FETCH_TASKS_SUCCESS,
  FETCH_TASKS_FAILURE,
  SHOW_CREATE_FORM
} from '../actionTypes';

const backend = 'https://api.taschengeldboerse.io';
const extractDataOrEmptyArray = (response) => (response.data) || [];

export const showCreateForm = () => ({ type: SHOW_CREATE_FORM });


function Sleep(milliseconds) {
  return new Promise(resolve => setTimeout(resolve, milliseconds));
}

const mapCategoryToTask = (categories) => (task) => {
  task.category = categories.find(c => c.id === task.category);

  const categoryIcons = {
    1: { icon:'directions_walk', color: '#16A085' },
    2: { icon:'shopping_cart', color: '#C0392B' },
    3: { icon:'spa', color: '#4CAF50' },
    4: { icon:'home', color: '#2980B9' },
    5: { icon:'pets', color: '#795548' },
    6: { icon:'computer', color: '#273C75' },
    7: { icon:'people', color: '#757575' },
  };

  const { icon, color } = categoryIcons[task.category.id];
  task.category.icon = icon;
  task.category.color = color;

  return task;
};

export const fetchTasks = () => async dispatch => {
  try {
    dispatch({ type: FETCH_TASKS_START });

    const resTasks = await axios.get(`${backend}/tasks`);
    const tasksArray = extractDataOrEmptyArray(resTasks);

    const resCategories = await axios.get(`${backend}/categories`);
    const categories = extractDataOrEmptyArray(resCategories);

    const tasks = tasksArray.map(mapCategoryToTask(categories));

    await Sleep(500);

    dispatch({ type: FETCH_TASKS_SUCCESS, payload: tasks });
  } catch (error) {
    dispatch({ type: FETCH_TASKS_FAILURE, payload: false });
  }
};

export const submitTask = () => async dispatch => {
  // try {
  //   dispatch({ type: FETCH_TASKS_START });
  //
  //   const res = await axios.get(`${backend}/tasks`);
  //   const extractDataOrEmptyArray = (response) => (response.data) || [];
  //
  //   await Sleep(500);
  //
  //   dispatch({ type: FETCH_TASKS_SUCCESS, payload: extractDataOrEmptyArray(res) });
  // } catch (error) {
  //   dispatch({ type: FETCH_TASKS_FAILURE, payload: false });
  // }
};
