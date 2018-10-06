import {
  SHOW_CREATE_FORM
} from '../actionTypes';

export default function(state = 'list', action) {
  switch (action.type) {
    case SHOW_CREATE_FORM:
      return 'form';
    default:
      return state;
  }
}
