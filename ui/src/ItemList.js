import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import Item from './Item';

import './ItemList.css';

class ItemList extends Component {
  constructor(props) {
    super(props);
    this.itemRefs = {};
  }

  changeFocus = (index) => {
    if (this.props.items.length > (index + 1)) {
      if (this.itemRefs[index + 1]) {
        this.itemRefs[index + 1].focus();
      }
    }
  }

  render() {
    var itemInputs = [];
    if (this.props.items) {
      itemInputs = this.props.items.map((item, index) =>
        <Item
          key={index}
          item={item}
          inputRef={(el) => {
            this.itemRefs[index] = el;
          }}
          index={index}
          changeFocus={this.changeFocus}
        /> 
      );
    }

    return (
      <div className="ItemList">
        {itemInputs}
      </div>
    );
  }
}

export default withRouter(ItemList);
