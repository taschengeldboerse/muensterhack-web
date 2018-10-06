import React, { Component } from 'react';
import Task from './Task';

class TaskList extends Component {
  render() {
    const { tasks } = this.props;

    if (!tasks) return null;

    return (
      <ul className="tasks">
        {tasks.length > 0 ? tasks.map((task, index) => {
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

export default TaskList;
