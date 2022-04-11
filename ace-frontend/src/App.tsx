import "./index.css";
import React, { Component } from "react";
import axios from "axios";

// Since React.Component automatically has a type of <Readonly {}>,
// a type must be made to define the props and the state.
// TODO: Add a type for the query that is returned / HINT: in the console

export default class App extends Component<{}, { todo_list: Array<any> }> {
  constructor(props: any) {
    super(props);
    this.state = {
      todo_list: [],
    };
  }

  // Everytime that the page is loaded, fetch again from Django.
  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      // Gets the response from the Django webserver
      .get("main/cardsets")
      // Deserializes the info given from serializer.py
      .then(res => this.setState({ todo_list: res.data }))
      // Catches any data error
      .catch(err => console.log(err));
  };

  // React component that returns all the cards in the list.
  renderItems = () => {
    const items = this.state.todo_list;
    console.log(this.state.todo_list);
    return items.map((item, index) => <p key={index}> {item.set_title} </p>);
    // TODO: add links for the cardsets, use url links from axios
  };

  render() {
    return <div className="p-5">{this.renderItems()}</div>;
  }
}
