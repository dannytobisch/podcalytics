import streamlit as st

# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading Dashboard ..."):
        #ast.shared.components.title_awesome("")
        st.write()
        st.title('Dashboard')

        user_input = st.text_input("Topic", 'data science')

        imgs = ['https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109',
                 'https://i.scdn.co/image/e7afa3e3cc009d133446a237bf4446832332db6e',
                 'https://i.scdn.co/image/c8eedefd77d737665a45537ace038aac90992db1',
                 'https://i.scdn.co/image/ef2c219df40ee75c10da01ad436e62e7cb86d625',
                 'https://i.scdn.co/image/d7f0c82c842a0e76c3c1e0ec8e10141929fa569c',
                 'https://i.scdn.co/image/2ee57ebd51928f159c849409bb66998becb7c668',
                 'https://i.scdn.co/image/c589a21e829672e24cebc5282b65fadf79fccf52',
                 'https://i.scdn.co/image/83d2d7b1570ffda9e0a9fa68cc54f6e43cbccfab',
                 'https://i.scdn.co/image/234c1d297baa1a87d44d1f46a590b60bae5bdd45',
                 'https://i.scdn.co/image/cade9c0a634cf2d953fd4337749969fa5771fffe',
                 'https://i.scdn.co/image/a53244522504e8c090a5d4818f1106ed1cf22291',
                 'https://i.scdn.co/image/71632d91700284ad526e5150fa5184918c124533',
                 'https://i.scdn.co/image/3f83019761fb2785a226517f3ff56fdac1f30e09',
                 'https://i.scdn.co/image/7469ac1dc82931691608b853a492863916e468ee',
                 'https://i.scdn.co/image/9963b90cb493a11d182545beb72e08cc189ae27f',
                 'https://i.scdn.co/image/8edac3cdd20433e67082896c27604397e5d7f94e',
                 'https://i.scdn.co/image/d8f603f06ec2c43a4bd5ee14c4488f1daa82120a',
                 'https://i.scdn.co/image/d7124e1ceb23250f9680e38dcad73e0e6f390990',
                 'https://i.scdn.co/image/160b31cc08717dea6d0d69549236f7d504eb2c3a',
                 'https://i.scdn.co/image/44560ff41d639c7c6f0aa1f3c5bd6aa0e17763b3',
                 'https://i.scdn.co/image/8251e54e9975231f9c671e4a88803f9b4b20f906',
                 'https://i.scdn.co/image/d1c1fb066ee0a897940c0e868ff77fe88134e1b4']


        url = ['https://open.spotify.com/show/63diy2DtpHzQfeNVxAPZgU',
               'https://open.spotify.com/show/1LaCr5TFAgYPK5qHjP3XDp',
               'https://open.spotify.com/show/1XeM2eOA7QM9ogjEU6aHBO',
               'https://open.spotify.com/show/0kp4abozqxCmILx0lT9foc',
               'https://open.spotify.com/show/5nrspdHxUxzc9TkEibpxD5',
               'https://open.spotify.com/show/71RbIpffwWXUMZQTFKiMWk',
               'https://open.spotify.com/show/57AJ6GiMDPVBLGRqvjeoz6',
               'https://open.spotify.com/show/1BZN7H3ikovSejhwQTzNm4',
               'https://open.spotify.com/show/7IbEWJjeimwddhOZqWe0G1',
               'https://open.spotify.com/show/0eaFZXUh8qys3c0Wr3vrA3',
               'https://open.spotify.com/show/02yJXEJAJiQ0Vm2AO9Xj6X',
               'https://open.spotify.com/show/3tE5An6N5P5VK531GZJ0tO',
               'https://open.spotify.com/show/5Kqi6CV44DNi85N4c9Lv5P',
               'https://open.spotify.com/show/1kAlMjcwRC55YfFWF8MGi3',
               'https://open.spotify.com/show/68SCv5gj6lf6kHM1EAbkAV',
               'https://open.spotify.com/show/529Q58D0db7bI8p6NKaRjU',
               'https://open.spotify.com/show/4Sacw5UzY7utm6coTEHS0h',
               'https://open.spotify.com/show/7yHiQn4eqjy2EAzRNEmQdf',
               'https://open.spotify.com/show/0tjehY4eNyO1RPvFLZjHS6',
               'https://open.spotify.com/show/3im5Z0T7hsaz9OMpYXFFwH',
               'https://open.spotify.com/show/3EEN9uPoV6PNqmKjoRDRXL',
               'https://open.spotify.com/show/6rnD1WdPdqlYiUdMUCEYli']

        st.components.v1.html(f'<div class="row">\
                  <div class="column">\
                  <a target="_blank" rel="noopener noreferrer"\
                  href="https://spotify.com"><img src="https://lh3.googleusercontent.com/UrY7BAZ-XfXGpfkeWg0zCCeo-7ras4DCoRalC_WXXWTK9q5b0Iw7B0YQMsVxZaNB7DM=s360-rw" width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                  href={url[1]}><img src={imgs[1]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%""></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[2]}><img src={imgs[2]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;padding-right:20px;border-radius:10%""></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                    href="https://youtube.com"><img src="https://stagewp.sharethis.com/wp-content/uploads/2018/02/youtube.png" width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;padding-left:2px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[4]}><img src="https://i.ytimg.com/vi/xC-c7E5PK0Y/default.jpg" width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[5]}><img src="https://i.ytimg.com/vi/X3paOmcrTjQ/default.jpg" width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  </div>\
                  <div class="column">\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[6]}><img src={imgs[6]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[0]}><img src={imgs[0]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[8]}><img src={imgs[8]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;padding-right:20px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[9]}><img src="https://i.ytimg.com/vi/4OZip0cgOho/default.jpg" width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;padding-left:2px;border-radius:10%"></a>\
                 <a target="_blank" rel="noopener noreferrer"\
                  href={url[10]}><img src="https://i.ytimg.com/vi/ua-CiDNNj30/default.jpg" width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[11]}><img src="https://i.ytimg.com/vi/Ck0ozfJV9-g/default.jpg" width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  </div>\
                  </div>', height=250)

        st.components.v1.html(f'<div class="row">\
                  <div class="column">\
                  <a target="_blank" rel="noopener noreferrer"\
                  href="https://medium.com"><img src="https://miro.medium.com/fit/c/256/256/1*6_fgYnisCa9V21mymySIvA.png" width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:50%;"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                  href={url[12]}><img src={imgs[12]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[13]}><img src={imgs[13]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;padding-right:20px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href="https://arxiv.org"><img src="https://pbs.twimg.com/profile_images/958432197987401728/QLeEVLC_.jpg" width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:50%;padding-left:2px"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[14]}><img src={imgs[14]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[15]}><img src={imgs[15]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  </div>\
                  <div class="column">\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[16]}><img src={imgs[16]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[17]}><img src={imgs[17]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[18]}><img src={imgs[18]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;padding-right:20px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[19]}><img src={imgs[19]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;padding-left:2px;border-radius:10%"></a>\
                 <a target="_blank" rel="noopener noreferrer"\
                  href={url[20]}><img src={imgs[20]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  <a target="_blank" rel="noopener noreferrer"\
                   href={url[21]}><img src={imgs[21]} width="100" height="100"\
                  style="vertical-align:middle;margin:3px 3px;border-radius:10%"></a>\
                  </div>\
                  </div>', height=250)
