% 载入图片
RGB = imread('huangdou.jpg');
I = rgb2gray(RGB);  %rgb转灰度图像
se = strel('disk',50); %圆盘型结构元素
I2 = imbothat(I,se);  % 底帽变换，去除不均匀背景
subplot(2,3,1);
imshow(I2);
title('预处理图像');

I3 = imadjust(I2);   % 调节灰度对比度


% 灰度图像二值化，全局阈值分割最大化类间方差
level = graythresh(I3);
BW = im2bw(I3,level);
subplot(2,3,2);
imshow(BW);
title('灰度二值化图像');
BW1=~BW; %图像取反
subplot(2,3,3);
imshow(BW1);
title('填充图像');
se1 = strel('disk',3);%用r为三的圆形结构元素开运算
BW2 = imopen(BW1,se1);
subplot(2,3,4);
imshow(BW2);
title('开运算');

[L,N] = bwlabel(BW2,4);  % N即为目标个数


% 标记目标物
subplot(2,3,5);
imshow(RGB);
title('结果');
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



