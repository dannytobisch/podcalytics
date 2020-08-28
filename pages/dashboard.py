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
                 'https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109',
                 'https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109',
                 'https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109',
                 'https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109',
                 'https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109',
                 'https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109',
                 'https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109',
                 'https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109',
                 'https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109',
                 'https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109',
                 'https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109',
                 'https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109',
                 'https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109',
                 'https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109',
                 'https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109',
                 'https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109',
                 'https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109',
                 'https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109',
                 'https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109',
                 'https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109',
                 'https://i.scdn.co/image/f149d28e02979195b0d2e649637b6ac44cd74109']


        url = ['https://open.spotify.com/episode/2dqPD9q8CeIlUlGWN1fXmU',
               'https://open.spotify.com/episode/142ZE0PABkLdcXTG1Dntap',
               'https://open.spotify.com/episode/2AccRfCb8MlPb6S2taZMRK',
               'https://open.spotify.com/episode/47c0IHcYjr2wFw6YXGAjaR',
               'https://open.spotify.com/episode/1xWon0SEaKs6nMh3acmNhy',
               'https://open.spotify.com/episode/21RFq0annWarqakU2ZC9O6',
               'https://open.spotify.com/episode/2emDmrJF0IIdTNjOO5Hys1',
               'https://open.spotify.com/episode/1pg6owCQws4YgPzTPwdD3s',
               'https://open.spotify.com/episode/5FFg5Pslcvi5E1b6c32sAV',
               'https://open.spotify.com/episode/2Ex8yaplUTJeD15hp5AkiP',
               'https://open.spotify.com/episode/6lnS9Xz55KSP92hR6pL9aH',
               'https://open.spotify.com/episode/3UBCQf2S0lo18S2xtqBCKh',
               'https://open.spotify.com/episode/20flI9imCj9YhW7HVUL92Z',
               'https://open.spotify.com/episode/0lf5LAuo1knnvWpwHPYKfq',
               'https://open.spotify.com/episode/6JOMkSAEY2ynISGe4goxBR',
               'https://open.spotify.com/episode/4DKphli6kcMKZio8ccKXoW',
               'https://open.spotify.com/episode/2HWkpJcfAABzDW2HHVxsAj',
               'https://open.spotify.com/episode/4Dhzr3lCWzDMe1OrUGjryP',
               'https://open.spotify.com/episode/0tHoeY76I5WBxcetcugZDZ',
               'https://open.spotify.com/episode/48XCjB7RhQaP5XgpKbPJFd',
               'https://open.spotify.com/episode/5Z84RmeUdxLmdtkMf4lLXY',
               'https://open.spotify.com/episode/3YUxN1FYSFXV6noTRxLcZV']

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
