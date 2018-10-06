import React, { Component } from 'react';
import { connect } from 'react-redux';

class Authenticated extends Component {
  render() {
    const { authenticated } = this.props;

    if (!authenticated) {
      return null;
    }

    return this.props.children;
  }
}

const mapStateToProps = state => ({ authenticated: state.auth.authenticated });

export default connect(mapStateToProps)(Authenticated);
