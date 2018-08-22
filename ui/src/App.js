import React, { Component } from 'react';
import { Route, Link } from 'react-router-dom';
import { Row, Col } from 'antd';
import logo from './logo.svg';
import './App.css';
import SignIn from './SignIn';
import Home from './Home';
import TestEdit from './TestEdit';
import TestList from './TestList';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      user: null
    };
  }

  handleAuthChange = (user) => {
    this.setState({
      user: user,
    });
  }

  render() {
    return (
      <div className="App">
        <Row
          type="flex"
          justify="space-between"
          className="navbar"
          align="middle"
          >
          <Col className="Logo"><Link to="/">Test Scoring</Link></Col>
          <Col><SignIn handleAuthChange={this.handleAuthChange} /></Col>
        </Row>
        <Route
          exact
          path="/"
          render={() => {
            return <Home signedInUser={this.state.user}/>;
          }}
        />
        <Route
          path={`/tests/:testId/edit`}
          render={() => {
            return <TestEdit/>;
          }}
        />
        <Route exact path={`/tests/:testType`} component={TestList}/>
      </div>
    );
  }
}

export default App;
