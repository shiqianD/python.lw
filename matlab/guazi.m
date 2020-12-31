% 载入图片
RGB = imread('h4.png');
I = rgb2gray(RGB);  %rgb转灰度图像
se = strel('disk',50);%圆盘型结构元素
I2 = imbothat(I,se);  % 底帽变换，去除不均匀背景
subplot(2,4,1);
imshow(I2);
title('预处理图像');

I3 = imadjust(I2);   % 调节灰度对比度

% 灰度图像二值化，全局阈值分割最大化类间方差
level = graythresh(I3);
BW = im2bw(I3,level);
subplot(2,4,2);
imshow(BW);
title('灰度二值化图像');

% 孔洞填充和形态学开运算
BW1 = imfill(BW,'holes');   %空洞填充
subplot(2,4,3);
imshow(BW1);
title('填充图像');
se1 = strel('square',10);%方型结构元素
BW2 = imopen(BW1,se1);  %开操作
subplot(2,4,4);
imshow(BW2);
title('开操作图像');


% 形态学腐蚀运算，部分目标物有粘连现象，去除粘连
se2 = strel('disk',3);%圆盘型结构元素
BW3 = imerode(BW2,se2); %形态学腐蚀
subplot(2,4,5);
imshow(BW3);
title('腐蚀一次');
BW4 = imerode(BW3,se2); %再次用se结构元素腐蚀
subplot(2,4,6);
imshow(BW4);
title('腐蚀两次');
BW5 = bwulterode(BW4);  %终极腐蚀
subplot(2,4,7);
imshow(BW5);
title('终极腐蚀');

[L,N] = bwlabel(BW5);  % N即为目标个数


% 标记目标物
subplot(2,4,8);
imshow(RGB);
title('计数标记');
hold on
for k = 1:N
    [r,c] = find(L == k);
    rbar = mean(r);
    cbar = mean(c);
    plot(cbar,rbar,'marker','*','markeredgecolor','b','markersize',10);
end


% 对话框显示目标物个数
h = dialog('Name','目标个数','position',[500 500 200 70]);  % 创建一个对话框窗口
uicontrol('Style','text','units','pixels','position',[45 40 120 20],...
    'fontsize',15,'parent',h,'string',num2str(N));     % 创建文本内容
uicontrol('units','pixels','position',[80 10 50 20],'fontsize',10,...
    'parent',h,'string','确定','callback','delete(gcf)'); % 创建【确定】按钮



