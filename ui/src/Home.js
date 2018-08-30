import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import { Spin } from 'antd';
import { Row, Input, Card, Modal, Button } from 'antd';
import StartTest from './StartTest';
import axios from 'axios';
import './Home.css';

class Home extends Component {

  state = {
  }

  componentDidMount() {
    this.wakeUpBackend();
  }

  wakeUpBackend = () => {
    axios.get('/up/')
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.log(error);
        Modal.error({
          title: "Unable to reach server",
          content: "Unable to reach server. Please refresh page and try again\n\n" + error + "\n\n" + JSON.stringify(error.response.data),
          maskClosable: true,
        })
      });
  }

  render() {
    if (!this.props.signedInUser) {
      return (
        <div className="Home">
          <h1>Welcome to Test Scoring</h1>
          Please sign in to continue
        </div>
      );
    }

    const assessments = [
      {
        slug: "cbcl_6_18",
        name: "CBCL 6-18"
      },
      {
        slug: "cbcl_1_5",
        name: "CBCL 1.5-5"
      }
    ]

    const startTests = assessments.map((assessment, index) =>
      <StartTest
        key={index}
        assessment={assessment}
      />
    );

    return (
      <div className="Home">
        <Row type="flex">
          {startTests}
        </Row>
      </div>
    );
  }
}

export default withRouter(Home);
