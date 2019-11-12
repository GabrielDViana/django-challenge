import React, { Component } from 'react';

import './App.css';
import 'antd/dist/antd.css';
import CustomLayout from './containers/Layouts';
import UpcomingLaunchList from './containers/UpcomingLaunchListView';
function App() {
  return (
    <div className="App">
      <CustomLayout>
        <UpcomingLaunchList />
      </CustomLayout>
    </div>
  );
}

export default App;
