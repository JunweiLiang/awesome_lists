
## Awesome Courses

An important part of being a professor is teaching. Here I collect a list of famous courses and share some personal thoughts on how they are technically managed.

优秀、开放的课程列表。



| Course                                            | Lecturer        | Org      | Link Type              | Link                                                                              |
|---------------------------------------------------|-----------------|----------|------------------------|-----------------------------------------------------------------------------------|
| python autograd/deep learning                     |                 | -        | Code                   | [link](https://github.com/geohot/tinygrad)                                                |
| python autograd/deep learning                     | Andrej Karpathy | -        | Code                   | [link](https://github.com/karpathy/micrograd)                                             |
|                                                   |                 |          | Lecture Video          | [link](https://www.youtube.com/watch?v=VMj-3S1tku0)                                       |
| python autograd/deep learning (11785/11685/11485) | Bhiksha Raj     | CMU      | Code                   | [link](https://github.com/CMU-IDeeL/new_grad)                                             |
|                                                   |                 |          | Course page            | [link](http://deeplearning.cs.cmu.edu/S21/index.html)                                     |
| computer vision general (cs231n)                  |                 | Stanford | Course page            | [link](http://cs231n.stanford.edu/)                                                       |
|                                                   |                 |          | Course notes page code | [link](https://github.com/cs231n)                                                         |
|                                                   |                 |          | nerf                   | [link](https://github.com/cs231n/cs231n.github.io/blob/master/nerf.md)                    |
|                                                   |                 |          | nerf                   | [link](https://github.com/cs231n/cs231n.github.io/blob/master/CS_231n__NeRF_write_up.pdf) |
| computer vision advanced (cs231a)                 |                 | Stanford | Course page            | [link](https://web.stanford.edu/class/cs231a/)                                            |
| Deep Learning Systems                             | Tianqi Chen     | CMU      | Course page            | [link](https://dlsyscourse.org/)                                                          |
| Story behind ResNet/ShuffleNet               | Xiangyu Zhang   | By [GAP Lab](https://gaplab.cuhk.edu.cn/)    | Lecture video           | [link](https://mp.weixin.qq.com/s?__biz=Mzg5NTc2MTA0NQ==&mid=2247487252&idx=1&sn=fd73ce6c0f0a7726eb9913fa9c7a41c0&chksm=c00a20eef77da9f8f72b020896b73238b817a329c6115bec3f942a3a4ff7600097e42af952ff&mpshare=1&scene=1&srcid=0901smoTXRMt3ddCcY0XwGNK&sharer_sharetime=1662005458842&sharer_shareid=c5b6fadc801a2c4ecd6ca0096153aea4&version=4.0.9.99149&platform=mac#rd)                                                          |
| Large-Scale Multimedia Analysis (11-775) |Alex Hauptmann  |CMU| Course page |[link](https://github.com/11775website/11775website.github.io)|
| Large-Scale Multimedia Analysis (11-775) |Alex Hauptmann |CMU| Homework Code|[link](https://github.com/11775website/11775-hws/tree/master/spring2021/hw1#submission-to-kaggle)|
| Intro to Transformers | Lucas Beyer | Google | slides | [link](https://docs.google.com/presentation/d/1ZXFIhYczos679r70Yu8vV9uO6B1J0ztzeDxbnBxD1S0/edit)|
|Deep Learning - NYU|Yann LeCun|NYU|Course page|[link](https://atcold.github.io/pytorch-Deep-Learning/)|
|Dive into Deep Learning|Mu Li|AWS|Course page|[link](https://space.bilibili.com/1567748478/channel/seriesdetail?sid=358497)|
||||Book|[link](https://zh.d2l.ai/)|

### Technicalities

Junwei: If you have a large course and want to take attendance record of students, you can set up after-class quizzes with this simple, mobile-friendly [webapp](https://github.com/JunweiLiang/Lecture_Attendance_Management)!  (which is previously used by [CMU LTI colloquium course](https://lti.cs.cmu.edu/lti-colloquium))

Junwei: I think cs231n has the cleanest model on how to make a good open-source course. They use a github repo to store all their course notes so that TAs and
even students can contribute to the notes and collaborate easily. The notes are in markdown format to ensure fast and easy change and Github will generate
corresponding html automatically (using jekyll). The downside is that you could not test them locally without compiling (each markdown file may include jekyll-specific code like layout imports).
So for not-so-rapidly-changing websites like personal page I would opt for static htmls which are easy to debug/refine locally.
But for course notes since people don't care how nice they looks so markdown is the way to go.

Junwei: When I was setting up homeworks for CMU 11-775 course, we found that having a leaderboard can motivate students to try out different ideas. And Kaggle is a free website where this can be done easily. Here is an example of [our homework](https://github.com/11775website/11775-hws/tree/master/spring2021/hw1) and [kaggle page](https://www.kaggle.com/competitions/11775-hw1/leaderboard).


