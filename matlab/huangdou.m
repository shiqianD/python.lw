% ����ͼƬ
RGB = imread('huangdou.jpg');
I = rgb2gray(RGB);  %rgbת�Ҷ�ͼ��
se = strel('disk',50); %Բ���ͽṹԪ��
I2 = imbothat(I,se);  % ��ñ�任��ȥ�������ȱ���
subplot(2,3,1);
imshow(I2);
title('Ԥ����ͼ��');

I3 = imadjust(I2);   % ���ڻҶȶԱȶ�


% �Ҷ�ͼ���ֵ����ȫ����ֵ�ָ������䷽��
level = graythresh(I3);
BW = im2bw(I3,level);
subplot(2,3,2);
imshow(BW);
title('�Ҷȶ�ֵ��ͼ��');
BW1=~BW; %ͼ��ȡ��
subplot(2,3,3);
imshow(BW1);
title('���ͼ��');
se1 = strel('disk',3);%��rΪ����Բ�νṹԪ�ؿ�����
BW2 = imopen(BW1,se1);
subplot(2,3,4);
imshow(BW2);
title('������');

[L,N] = bwlabel(BW2,4);  % N��ΪĿ�����


% ���Ŀ����
subplot(2,3,5);
imshow(RGB);
title('���');
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



