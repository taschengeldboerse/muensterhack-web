import React, { Component } from 'react';

import Footer from '../components/Footer';

export default class Layout extends Component {
  render() {
    const { children } = this.props;

    return (
      <div className="page-wrapper">
        <div className="content-wrap">{children}</div>
        {/*<div className="kiosk-footer">*/}
          {/*<Footer />*/}
          {/*{this.renderButton()}*/}
        {/*</div>*/}
      </div>
    );
  }

  renderButton() {
    const { button } = this.props;
    if (!button) return null;

    return <div className="main-button-wrapper">{button}</div>;
  }
}
