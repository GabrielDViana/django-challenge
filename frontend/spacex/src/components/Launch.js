import React from 'react';

import { List, Avatar, Icon } from 'antd';


const IconText = ({ type, text }) => (
    <span>
        <Icon type={type} style={{ marginRight: 8 }} />
        {text}
    </span>
);

const Launch = (props) => {
    return (
        <List
            itemLayout="vertical"
            size="large"
            pagination={{
                onChange: page => {
                    console.log(page);
                },
                pageSize: 3,
            }}
            dataSource={props.data}
            footer={
                <div>
                    <b>ant design</b> footer part
      </div>
            }
            renderItem={item => (
                <List.Item
                
                    actions={[
                        <IconText type="star-o" text="156" key="list-vertical-star-o" />,
                        <IconText type="like-o" text="156" key="list-vertical-like-o" />,
                        <IconText type="message" text="2" key="list-vertical-message" />,
                    ]}
                    extra={
                        <img
                            width={272}
                            alt="logo"
                            src="https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png"
                        />
                    }
                >
                    {/* flight_number
                    launch_year
                    launch_date_utc
                    launch_date_local
                    rocket_id
                    rocket_name
                    rocket_type
                    land_success
                    site_name
                    customer
                    nationality
                    manufacturer
                    launch_success */}
                    <List.Item.Meta
                        // avatar={<Avatar src={item.avatar} />}
                        title={item.rocket_name}
                        description={item.nationality}
                    />
                    {item.manufacturer}
                </List.Item>
            )}
        />
    );
}

export default Launch;