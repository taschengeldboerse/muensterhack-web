import React, { Component } from 'react';
import { Provider } from 'react-redux';
import Authenticated from './container/Authenticated';
import Switch from './container/Switch'
import './App.css';

import store from './store/configureStore';
import Signin from './container/Signin';

class App extends Component {

  render() {
    return (
      <Provider store={store}>
        <div className="wrapper">
          <h2 className="title">Taschengeldbörse</h2>
          <Signin />
          <Authenticated>
            <Switch />
          </Authenticated>
        </div>
      </Provider>
    );
  }
}

export default App;