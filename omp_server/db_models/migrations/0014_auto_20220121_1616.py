# Generated by Django 3.1.4 on 2022-01-21 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_models', '0013_merge_20220114_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLoginLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, verbose_name='Username')),
                ('login_time', models.DateTimeField(blank=True, null=True, verbose_name='Login time')),
                ('ip', models.CharField(blank=True, max_length=32, null=True, verbose_name='Login ip')),
                ('role', models.CharField(blank=True, max_length=128, null=True, verbose_name='role ')),
            ],
            options={
                'verbose_name': '用户登陆记录',
                'verbose_name_plural': '用户登陆记录',
                'db_table': 'omp_login_log',
            },
        ),
        migrations.AlterField(
            model_name='backuphistory',
            name='content',
            field=models.JSONField(verbose_name='备份内容(实例名):["mysql1","arangodb2"]'),
        ),
        migrations.AlterField(
            model_name='backuphistory',
            name='retain_path',
            field=models.TextField(default='/data/omp/data/backup/', verbose_name='文件保存路径'),
        ),
        migrations.AlterField(
            model_name='backupsetting',
            name='retain_path',
            field=models.TextField(default='/data/omp/data/backup/', verbose_name='文件保存路径'),
        ),
    ]
