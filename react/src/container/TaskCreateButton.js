import React, { Component } from 'react';
import { connect } from 'react-redux';
import { showCreateForm } from '../store/actions/tasks';

class TaskCreateButton extends Component {

  render() {
    const { showCreateForm } = this.props;

    return (
      <button className="button is-primary fab-bottom" type="submit" onClick={showCreateForm}>
        Hilfe anfragen
      </button>
    );
  }
}

const mapStateToProps = state => ({ view: state.view });
const mapDispatchToProps = { showCreateForm };

export default connect(mapStateToProps, mapDispatchToProps)(TaskCreateButton);
