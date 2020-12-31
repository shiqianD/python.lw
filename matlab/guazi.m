% ����ͼƬ
RGB = imread('h4.png');
I = rgb2gray(RGB);  %rgbת�Ҷ�ͼ��
se = strel('disk',50);%Բ���ͽṹԪ��
I2 = imbothat(I,se);  % ��ñ�任��ȥ�������ȱ���
subplot(2,4,1);
imshow(I2);
title('Ԥ����ͼ��');

I3 = imadjust(I2);   % ���ڻҶȶԱȶ�

% �Ҷ�ͼ���ֵ����ȫ����ֵ�ָ������䷽��
level = graythresh(I3);
BW = im2bw(I3,level);
subplot(2,4,2);
imshow(BW);
title('�Ҷȶ�ֵ��ͼ��');

% �׶�������̬ѧ������
BW1 = imfill(BW,'holes');   %�ն����
subplot(2,4,3);
imshow(BW1);
title('���ͼ��');
se1 = strel('square',10);%���ͽṹԪ��
BW2 = imopen(BW1,se1);  %������
subplot(2,4,4);
imshow(BW2);
title('������ͼ��');


% ��̬ѧ��ʴ���㣬����Ŀ������ճ������ȥ��ճ��
se2 = strel('disk',3);%Բ���ͽṹԪ��
BW3 = imerode(BW2,se2); %��̬ѧ��ʴ
subplot(2,4,5);
imshow(BW3);
title('��ʴһ��');
BW4 = imerode(BW3,se2); %�ٴ���se�ṹԪ�ظ�ʴ
subplot(2,4,6);
imshow(BW4);
title('��ʴ����');
BW5 = bwulterode(BW4);  %�ռ���ʴ
subplot(2,4,7);
imshow(BW5);
title('�ռ���ʴ');

[L,N] = bwlabel(BW5);  % N��ΪĿ�����


% ���Ŀ����
subplot(2,4,8);
imshow(RGB);
title('�������');
hold on
for k = 1:N
    [r,c] = find(L == k);
    rbar = mean(r);
    cbar = mean(c);
    plot(cbar,rbar,'marker','*','markeredgecolor','b','markersize',10);
end


% �Ի�����ʾĿ�������
h = dialog('Name','Ŀ�����','position',[500 500 200 70]);  % ����һ���Ի��򴰿�
uicontrol('Style','text','units','pixels','position',[45 40 120 20],...
    'fontsize',15,'parent',h,'string',num2str(N));     % �����ı�����
uicontrol('units','pixels','position',[80 10 50 20],'fontsize',10,...
    'parent',h,'string','ȷ��','callback','delete(gcf)'); % ������ȷ������ť



