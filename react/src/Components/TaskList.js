import React, { Component } from 'react';
import Task from './TaskList';

class App extends Component {
  render() {
    const { tasks } = this.props;

    return (
      <ul className="tasks">
        {tasks.length > 0 ? this.state.tasks.map((task, index) => {
          return (
            <li className="task" key={`task-${index}`}>
              <Task task={task} />
            </li>
          )
        }) : null}
      </ul>
    );
  }
}

export default App;
