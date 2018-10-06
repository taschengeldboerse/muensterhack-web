import { combineReducers } from 'redux';
import { reducer as form } from 'redux-form';

import auth from './auth';
import tasks from './tasks';
import view from './view';

const rootReducer = combineReducers({
  auth,
  form,
  tasks,
  view,
});

export default rootReducer;
