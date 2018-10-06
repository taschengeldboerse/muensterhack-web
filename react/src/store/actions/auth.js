import axios from 'axios';
import {
  AUTHENTICATED,
  UNAUTHENTICATED,
  AUTHENTICATION_ERROR,
  SET_AVAILABLE,
} from '../actionTypes';

export const signOutAction = () => {
  localStorage.clear();
  return {
    type: UNAUTHENTICATED,
  };
};

export const signInAction = ({ firstname, lastname }) => async dispatch => {
  try {
    // const res = await axios.post(`/api/guest/signin`, { firstname, lastname });
    dispatch({ type: AUTHENTICATED });
    // localStorage.setItem('user', res.data.token);
  } catch (error) {
    dispatch({
      type: AUTHENTICATION_ERROR,
      payload: 'Invalid credentials',
    });
  }
};
