create table discordstudents
(
    discorduserid bigint not null primary key,
    onecguid      varchar(36) not null
);

alter table discordstudents
    owner to pritexx;
