import React, { Component } from 'react';

import './App.css';
import 'antd/dist/antd.css';
import CustomLayout from './containers/Layouts';
import LaunchList from './containers/LaunchListView';
function App() {
  return (
    <div className="App">
      <CustomLayout>
        <LaunchList />
      </CustomLayout>
    </div>
  );
}

export default App;
