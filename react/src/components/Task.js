import React, { Component } from 'react';

class Task extends Component {
  render() {
    const {
      category,
      description,
      due_date,
      distance_in_meters,
      estimated_time_in_minutes,
      title,
    } = this.props.task;

    return (
      <>
        <div className="top">
          <div className="category">
            <i className="material-icons" style={{ color: category.color }}>{category.icon}</i>
            {category.name}
          </div>
          {!!distance_in_meters ?
            <>
              {distance_in_meters} m
              <div className="distance">
                <i className="material-icons">navigation</i>
              </div>
            </>
            : null}
        </div>
        <div className="title">
          {title}
        </div>
        <div className="description">
          {description}
        </div>
        <div className="bottom">
          <div className="estimated_time">
            <i className="material-icons">timer</i>
            ca. {estimated_time_in_minutes} Minuten
          </div>
          <div className="duedate">
            bis zum {new Date(due_date).toLocaleDateString()}
            <i className="material-icons">date_range</i>
          </div>
        </div>
      </>
    );
  }
}

export default Task;
