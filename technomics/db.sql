--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO geethu;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: geethu
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO geethu;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: geethu
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO geethu;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: geethu
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO geethu;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: geethu
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO geethu;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: geethu
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO geethu;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: geethu
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO geethu;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO geethu;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: geethu
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO geethu;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: geethu
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: geethu
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO geethu;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: geethu
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO geethu;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: geethu
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO geethu;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: geethu
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    content_type_id integer,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO geethu;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: geethu
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO geethu;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: geethu
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO geethu;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: geethu
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO geethu;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: geethu
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO geethu;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO geethu;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: geethu
--

CREATE SEQUENCE django_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO geethu;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: geethu
--

ALTER SEQUENCE django_site_id_seq OWNED BY django_site.id;


--
-- Name: south_migrationhistory; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE south_migrationhistory (
    id integer NOT NULL,
    app_name character varying(255) NOT NULL,
    migration character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.south_migrationhistory OWNER TO geethu;

--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE; Schema: public; Owner: geethu
--

CREATE SEQUENCE south_migrationhistory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.south_migrationhistory_id_seq OWNER TO geethu;

--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: geethu
--

ALTER SEQUENCE south_migrationhistory_id_seq OWNED BY south_migrationhistory.id;


--
-- Name: thumbnail_kvstore; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE thumbnail_kvstore (
    key character varying(200) NOT NULL,
    value text NOT NULL
);


ALTER TABLE public.thumbnail_kvstore OWNER TO geethu;

--
-- Name: web_aboutus; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE web_aboutus (
    dates_ptr_id integer NOT NULL,
    title character varying(100),
    description text
);


ALTER TABLE public.web_aboutus OWNER TO geethu;

--
-- Name: web_blog; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE web_blog (
    dates_ptr_id integer NOT NULL,
    title character varying(500),
    description text,
    author character varying(80) NOT NULL
);


ALTER TABLE public.web_blog OWNER TO geethu;

--
-- Name: web_comment; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE web_comment (
    dates_ptr_id integer NOT NULL,
    blog_id_id integer NOT NULL,
    author character varying(80) NOT NULL,
    description text
);


ALTER TABLE public.web_comment OWNER TO geethu;

--
-- Name: web_contactus; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE web_contactus (
    dates_ptr_id integer NOT NULL,
    name character varying(80) NOT NULL,
    email_id character varying(75) NOT NULL,
    message text
);


ALTER TABLE public.web_contactus OWNER TO geethu;

--
-- Name: web_dates; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE web_dates (
    id integer NOT NULL,
    created_date timestamp with time zone,
    modified_date timestamp with time zone
);


ALTER TABLE public.web_dates OWNER TO geethu;

--
-- Name: web_dates_id_seq; Type: SEQUENCE; Schema: public; Owner: geethu
--

CREATE SEQUENCE web_dates_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.web_dates_id_seq OWNER TO geethu;

--
-- Name: web_dates_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: geethu
--

ALTER SEQUENCE web_dates_id_seq OWNED BY web_dates.id;


--
-- Name: web_feature; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE web_feature (
    dates_ptr_id integer NOT NULL,
    title character varying(100),
    description text,
    image character varying(100) NOT NULL
);


ALTER TABLE public.web_feature OWNER TO geethu;

--
-- Name: web_homepage; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE web_homepage (
    dates_ptr_id integer NOT NULL,
    logo character varying(100) NOT NULL,
    customer_care character varying(50)
);


ALTER TABLE public.web_homepage OWNER TO geethu;

--
-- Name: web_newsevents; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE web_newsevents (
    dates_ptr_id integer NOT NULL,
    title character varying(100),
    description text,
    event_date timestamp with time zone NOT NULL,
    image character varying(100)
);


ALTER TABLE public.web_newsevents OWNER TO geethu;

--
-- Name: web_services; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE web_services (
    dates_ptr_id integer NOT NULL,
    title character varying(100),
    banner_image character varying(100) NOT NULL,
    content_subhead character varying(100),
    description text
);


ALTER TABLE public.web_services OWNER TO geethu;

--
-- Name: web_services_section; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE web_services_section (
    dates_ptr_id integer NOT NULL,
    section_head character varying(100),
    section_image character varying(100) NOT NULL,
    description text
);


ALTER TABLE public.web_services_section OWNER TO geethu;

--
-- Name: web_slide; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE web_slide (
    dates_ptr_id integer NOT NULL,
    text character varying(200),
    image character varying(100) NOT NULL,
    slideshow_id_id integer NOT NULL
);


ALTER TABLE public.web_slide OWNER TO geethu;

--
-- Name: web_slideshow; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE web_slideshow (
    dates_ptr_id integer NOT NULL,
    left_arrow character varying(100) NOT NULL,
    right_arrow character varying(100) NOT NULL,
    max_slide_count integer NOT NULL,
    bullet_active character varying(100) NOT NULL,
    bullet_inactive character varying(100) NOT NULL
);


ALTER TABLE public.web_slideshow OWNER TO geethu;

--
-- Name: web_testimonials; Type: TABLE; Schema: public; Owner: geethu; Tablespace: 
--

CREATE TABLE web_testimonials (
    dates_ptr_id integer NOT NULL,
    title character varying(100),
    description text,
    image character varying(100) NOT NULL
);


ALTER TABLE public.web_testimonials OWNER TO geethu;

--
-- Name: id; Type: DEFAULT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY django_site ALTER COLUMN id SET DEFAULT nextval('django_site_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY south_migrationhistory ALTER COLUMN id SET DEFAULT nextval('south_migrationhistory_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY web_dates ALTER COLUMN id SET DEFAULT nextval('web_dates_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: geethu
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: geethu
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add permission	1	add_permission
2	Can change permission	1	change_permission
3	Can delete permission	1	delete_permission
4	Can add group	2	add_group
5	Can change group	2	change_group
6	Can delete group	2	delete_group
7	Can add user	3	add_user
8	Can change user	3	change_user
9	Can delete user	3	delete_user
10	Can add content type	4	add_contenttype
11	Can change content type	4	change_contenttype
12	Can delete content type	4	delete_contenttype
13	Can add session	5	add_session
14	Can change session	5	change_session
15	Can delete session	5	delete_session
16	Can add site	6	add_site
17	Can change site	6	change_site
18	Can delete site	6	delete_site
19	Can add log entry	7	add_logentry
20	Can change log entry	7	change_logentry
21	Can delete log entry	7	delete_logentry
22	Can add kv store	8	add_kvstore
23	Can change kv store	8	change_kvstore
24	Can delete kv store	8	delete_kvstore
25	Can add migration history	9	add_migrationhistory
26	Can change migration history	9	change_migrationhistory
27	Can delete migration history	9	delete_migrationhistory
28	Can add dates	10	add_dates
29	Can change dates	10	change_dates
30	Can delete dates	10	delete_dates
31	Can add homepage	11	add_homepage
32	Can change homepage	11	change_homepage
33	Can delete homepage	11	delete_homepage
34	Can add feature	12	add_feature
35	Can change feature	12	change_feature
36	Can delete feature	12	delete_feature
37	Can add newsevents	13	add_newsevents
38	Can change newsevents	13	change_newsevents
39	Can delete newsevents	13	delete_newsevents
40	Can add aboutus	14	add_aboutus
41	Can change aboutus	14	change_aboutus
42	Can delete aboutus	14	delete_aboutus
43	Can add contactus	15	add_contactus
44	Can change contactus	15	change_contactus
45	Can delete contactus	15	delete_contactus
46	Can add blog	16	add_blog
47	Can change blog	16	change_blog
48	Can delete blog	16	delete_blog
49	Can add comment	17	add_comment
50	Can change comment	17	change_comment
51	Can delete comment	17	delete_comment
52	Can add services	18	add_services
53	Can change services	18	change_services
54	Can delete services	18	delete_services
55	Can add services_section	19	add_services_section
56	Can change services_section	19	change_services_section
57	Can delete services_section	19	delete_services_section
58	Can add testimonials	20	add_testimonials
59	Can change testimonials	20	change_testimonials
60	Can delete testimonials	20	delete_testimonials
61	Can add slideshow	21	add_slideshow
62	Can change slideshow	21	change_slideshow
63	Can delete slideshow	21	delete_slideshow
64	Can add Slides	22	add_slide
65	Can change Slides	22	change_slide
66	Can delete Slides	22	delete_slide
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: geethu
--

SELECT pg_catalog.setval('auth_permission_id_seq', 66, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$10000$wV4RiYkz81ax$D+Z/CUWXkeh1Lfmq5vVl0eCzqBP/TXmz5H0uqycz1kU=	2013-09-20 13:12:22.758831+05:30	t	geethu			geethusureh@gmail.com	t	t	2013-07-18 10:34:23.926836+05:30
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: geethu
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: geethu
--

SELECT pg_catalog.setval('auth_user_id_seq', 1, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: geethu
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY django_admin_log (id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message) FROM stdin;
1	2013-07-20 21:27:49.79046+05:30	1	12	1	Feature object	1	
2	2013-07-20 21:31:37.063416+05:30	1	11	2	Homepage object	1	
3	2013-07-20 21:35:46.377918+05:30	1	20	3	Testimonials object	1	
4	2013-07-20 21:37:20.027646+05:30	1	21	4	Slideshow object	1	
5	2013-07-20 21:42:07.89684+05:30	1	14	5	Aboutus object	1	
6	2013-07-20 21:45:03.385788+05:30	1	21	4	Slideshow object	3	
7	2013-07-20 21:45:37.186199+05:30	1	21	6	Slideshow object	1	
8	2013-07-22 12:02:31.492635+05:30	1	11	2	Homepage object	3	
9	2013-07-22 12:03:47.48745+05:30	1	11	7	Homepage object	1	
10	2013-07-22 12:06:12.471425+05:30	1	21	6	Slideshow object	3	
11	2013-07-22 12:06:53.852102+05:30	1	21	8	Slideshow object	1	
12	2013-07-22 12:07:39.571585+05:30	1	11	7	Homepage object	3	
13	2013-07-22 12:08:03.90152+05:30	1	11	9	Homepage object	1	
14	2013-07-23 13:47:14.909667+05:30	1	13	11	News & Events	1	
15	2013-07-24 21:27:58.800009+05:30	1	21	12	Slideshow object	1	
16	2013-07-24 21:28:11.062051+05:30	1	21	8	Slideshow object	3	
17	2013-07-24 22:59:46.776898+05:30	1	21	12	Slideshow object	3	
18	2013-07-24 23:09:41.022361+05:30	1	21	13	Slideshow object	1	
19	2013-07-26 13:19:16.913026+05:30	1	21	13	Slideshow object	3	
20	2013-07-26 13:59:30.914165+05:30	1	21	17	Slideshow object	1	
21	2013-07-26 14:01:32.65258+05:30	1	21	17	Slideshow object	3	
22	2013-07-26 14:07:26.479245+05:30	1	21	22	Slideshow object	1	
23	2013-07-26 14:08:32.537273+05:30	1	21	22	Slideshow object	3	
24	2013-07-26 14:10:23.496479+05:30	1	21	26	Slideshow object	1	
25	2013-07-26 14:12:55.253292+05:30	1	21	26	Slideshow object	3	
26	2013-07-26 14:14:47.693472+05:30	1	21	30	Slideshow object	1	
27	2013-07-27 15:37:55.398164+05:30	1	16	34	Wanted Marketing Executives 	1	
28	2013-07-27 15:38:39.987077+05:30	1	16	35	Wanted Developers with 4 yrs experience	1	
29	2013-07-27 15:39:28.485831+05:30	1	16	36	Started our new office in kadavanthra	1	
30	2013-07-27 16:21:13.729799+05:30	1	16	34	Wanted Marketing Executives 	2	Changed description.
31	2013-07-27 16:21:23.861815+05:30	1	16	35	Wanted Developers with 4 yrs experience	2	Changed description.
32	2013-07-27 16:21:40.426441+05:30	1	16	36	Started our new office in kadavanthra	2	Changed description.
33	2013-07-29 11:59:29.375052+05:30	1	21	37	Slideshow object	1	
34	2013-07-29 15:01:07.36661+05:30	1	21	37	Slideshow object	3	
35	2013-07-29 15:03:10.445146+05:30	1	21	30	Slideshow object	2	Changed image for Slides "Slide object". Changed image for Slides "Slide object".
36	2013-07-29 15:03:28.757996+05:30	1	21	30	Slideshow object	2	No fields changed.
37	2013-07-29 15:21:26.44664+05:30	1	21	30	Slideshow object	2	Changed text for Slides "Slide object".
38	2013-07-29 16:50:31.212395+05:30	1	21	30	Slideshow object	2	Changed text for Slides "Slide object". Changed text for Slides "Slide object".
39	2013-07-29 16:54:21.636687+05:30	1	21	30	Slideshow object	2	Changed text for Slides "Slide object". Changed text for Slides "Slide object". Changed text for Slides "Slide object".
40	2013-07-30 17:54:09.89922+05:30	1	18	62	Services object	1	
41	2013-07-30 17:54:53.187813+05:30	1	19	63	Services_section object	1	
42	2013-07-30 17:55:19.032826+05:30	1	19	64	Services_section object	1	
43	2013-09-20 13:17:23.572298+05:30	1	21	88	Slideshow object	1	
44	2013-09-20 13:18:06.776075+05:30	1	11	91	Homepage object	1	
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: geethu
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 44, true);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	permission	auth	permission
2	group	auth	group
3	user	auth	user
4	content type	contenttypes	contenttype
5	session	sessions	session
6	site	sites	site
7	log entry	admin	logentry
8	kv store	thumbnail	kvstore
9	migration history	south	migrationhistory
10	dates	web	dates
11	homepage	web	homepage
12	feature	web	feature
13	newsevents	web	newsevents
14	aboutus	web	aboutus
15	contactus	web	contactus
16	blog	web	blog
17	comment	web	comment
18	services	web	services
19	services_section	web	services_section
20	testimonials	web	testimonials
21	slideshow	web	slideshow
22	Slides	web	slide
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: geethu
--

SELECT pg_catalog.setval('django_content_type_id_seq', 22, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
m3shmj8pj1b4bvsu2gvfpkh9t9z36ddy	ZjhhMWNiOWQ0M2JkN2E3OWNmYzYwNDVjMTI2MGUwZGE3YTU1NDFiNjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu	2013-08-10 15:32:55.938132+05:30
834i8fxb3qloy1j8qvc4x3flydjhrbev	ZjhhMWNiOWQ0M2JkN2E3OWNmYzYwNDVjMTI2MGUwZGE3YTU1NDFiNjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu	2013-08-15 10:09:52.763333+05:30
qg5busfdmwenuk5geml4qp0lmrgnftcq	ZjhhMWNiOWQ0M2JkN2E3OWNmYzYwNDVjMTI2MGUwZGE3YTU1NDFiNjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu	2013-08-19 14:57:22.986439+05:30
dn0lwytchrmsl9szbncpq3oc1cv76nnc	ZjhhMWNiOWQ0M2JkN2E3OWNmYzYwNDVjMTI2MGUwZGE3YTU1NDFiNjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu	2013-09-06 10:35:45.108372+05:30
p71vkg8wbr3w8o9466ph1okbaw4nunuc	ZjhhMWNiOWQ0M2JkN2E3OWNmYzYwNDVjMTI2MGUwZGE3YTU1NDFiNjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu	2013-10-04 13:12:22.814491+05:30
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY django_site (id, domain, name) FROM stdin;
1	example.com	example.com
\.


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: geethu
--

SELECT pg_catalog.setval('django_site_id_seq', 1, true);


--
-- Data for Name: south_migrationhistory; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY south_migrationhistory (id, app_name, migration, applied) FROM stdin;
1	web	0001_initial	2013-07-18 10:36:28.960692+05:30
2	web	0002_auto__add_services_section__add_homepage__add_aboutus__add_services__a	2013-07-19 16:16:12.238212+05:30
3	web	0003_auto__add_slide__chg_field_newsevents_image__del_field_slideshow_image	2013-07-24 17:50:22.152532+05:30
4	web	0004_auto__add_field_slideshow_bullet_active__add_field_slideshow_bullet_in	2013-07-26 14:06:55.364291+05:30
\.


--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: geethu
--

SELECT pg_catalog.setval('south_migrationhistory_id_seq', 4, true);


--
-- Data for Name: thumbnail_kvstore; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY thumbnail_kvstore (key, value) FROM stdin;
sorl-thumbnail||image||77bddb23aeb6a8e0b359d4f1bce7a420	{"storage": "django.core.files.storage.FileSystemStorage", "name": "uploads/images/logo.jpg", "size": [193, 66]}
sorl-thumbnail||image||68979b2029a0ab47b742e4c4ebcbda2c	{"storage": "django.core.files.storage.FileSystemStorage", "name": "cache/f4/52/f4529b0fb8fea10f871a0374db54f6fe.jpg", "size": [200, 68]}
sorl-thumbnail||thumbnails||77bddb23aeb6a8e0b359d4f1bce7a420	["68979b2029a0ab47b742e4c4ebcbda2c"]
sorl-thumbnail||image||7d14e178dd816603f3d5026ffc5e190a	{"storage": "django.core.files.storage.FileSystemStorage", "name": "uploads/images/lap.jpg", "size": [252, 91]}
sorl-thumbnail||image||e2e9ce031b5df5ac04f5a7e2676947d7	{"storage": "django.core.files.storage.FileSystemStorage", "name": "cache/0b/4a/0b4a476f30970213c0655eebb03bc8a8.jpg", "size": [200, 72]}
sorl-thumbnail||thumbnails||7d14e178dd816603f3d5026ffc5e190a	["e2e9ce031b5df5ac04f5a7e2676947d7"]
sorl-thumbnail||image||d4eec3c7e2a76f0ba36276fa5dde8109	{"storage": "django.core.files.storage.FileSystemStorage", "name": "uploads/images/leftArrow.png", "size": [66, 66]}
sorl-thumbnail||image||3e5979c158b45413d437e6775415d9f9	{"storage": "django.core.files.storage.FileSystemStorage", "name": "cache/0e/62/0e62b4a44180abad158fb09d763a06e7.jpg", "size": [200, 200]}
sorl-thumbnail||thumbnails||d4eec3c7e2a76f0ba36276fa5dde8109	["3e5979c158b45413d437e6775415d9f9"]
sorl-thumbnail||image||c687134234bc6dc3bc15d343b5225ded	{"storage": "django.core.files.storage.FileSystemStorage", "name": "uploads/images/rightArrow.png", "size": [67, 66]}
sorl-thumbnail||image||984fa53d9fe0250df012085d6cfc4a24	{"storage": "django.core.files.storage.FileSystemStorage", "name": "cache/7c/93/7c93a3a2952e71ee05d1c02bcaad8c10.jpg", "size": [200, 197]}
sorl-thumbnail||thumbnails||c687134234bc6dc3bc15d343b5225ded	["984fa53d9fe0250df012085d6cfc4a24"]
sorl-thumbnail||image||ee6b628be5ca190324432c367b3d0871	{"storage": "django.core.files.storage.FileSystemStorage", "name": "uploads/images/redDot.png", "size": [19, 19]}
sorl-thumbnail||image||c5ff593b18971f8406b491fff0458ffe	{"storage": "django.core.files.storage.FileSystemStorage", "name": "cache/13/d6/13d61fa148b561375808468985b079cd.jpg", "size": [200, 200]}
sorl-thumbnail||thumbnails||ee6b628be5ca190324432c367b3d0871	["c5ff593b18971f8406b491fff0458ffe"]
sorl-thumbnail||image||f9fec9f8252ceeb4836bc8cdbf2e178d	{"storage": "django.core.files.storage.FileSystemStorage", "name": "uploads/images/whiteDot.png", "size": [19, 19]}
sorl-thumbnail||image||d4a66edc62eda173bb360c721bf0294d	{"storage": "django.core.files.storage.FileSystemStorage", "name": "cache/3a/53/3a5356124fc7322a43b8d7bc2ef958b2.jpg", "size": [200, 200]}
sorl-thumbnail||thumbnails||f9fec9f8252ceeb4836bc8cdbf2e178d	["d4a66edc62eda173bb360c721bf0294d"]
sorl-thumbnail||image||2814b1d3debadfc4b89cb79255c4a100	{"storage": "django.core.files.storage.FileSystemStorage", "name": "uploads/images/banner.png", "size": [1550, 477]}
sorl-thumbnail||image||0ee4bf29556cab6d5b26a6fcf9d04234	{"storage": "django.core.files.storage.FileSystemStorage", "name": "cache/a9/a6/a9a6ce0801980cbf1c1ff51a682f0bed.jpg", "size": [200, 62]}
sorl-thumbnail||thumbnails||2814b1d3debadfc4b89cb79255c4a100	["0ee4bf29556cab6d5b26a6fcf9d04234"]
sorl-thumbnail||image||140fb474b71133a8506559354cb9e0b2	{"storage": "django.core.files.storage.FileSystemStorage", "name": "uploads/images/Capture.PNG", "size": [947, 323]}
sorl-thumbnail||image||3d1bf0ab7afe1bc17dd4286fe67a91fa	{"storage": "django.core.files.storage.FileSystemStorage", "name": "cache/dc/d9/dcd99184959812ad512eed8a46200597.jpg", "size": [200, 68]}
sorl-thumbnail||thumbnails||140fb474b71133a8506559354cb9e0b2	["3d1bf0ab7afe1bc17dd4286fe67a91fa"]
sorl-thumbnail||image||334880833d228cea5d1051c3c5235f89	{"storage": "django.core.files.storage.FileSystemStorage", "name": "uploads/images/Capture1.PNG", "size": [948, 323]}
sorl-thumbnail||image||cfd0da237ee3a339ccbdfb69a5436e42	{"storage": "django.core.files.storage.FileSystemStorage", "name": "cache/c4/a4/c4a4b192c032cfdc048d068a24d6a921.jpg", "size": [200, 68]}
sorl-thumbnail||thumbnails||334880833d228cea5d1051c3c5235f89	["cfd0da237ee3a339ccbdfb69a5436e42"]
sorl-thumbnail||image||ebe325aa6ca107e664011670c2e0a821	{"storage": "django.core.files.storage.FileSystemStorage", "name": "uploads/images/bannerr.jpg", "size": [1550, 477]}
sorl-thumbnail||image||416801fe9e30595159f804bf093ef019	{"storage": "django.core.files.storage.FileSystemStorage", "name": "cache/50/fc/50fc1ba926409a88f0a3f1f231569886.jpg", "size": [200, 62]}
sorl-thumbnail||thumbnails||ebe325aa6ca107e664011670c2e0a821	["416801fe9e30595159f804bf093ef019"]
sorl-thumbnail||image||f97b805222cce6260e2daf0649dc3a70	{"storage": "django.core.files.storage.FileSystemStorage", "name": "uploads/images/banr.jpg", "size": [1550, 477]}
sorl-thumbnail||image||de1a101b78064620e0a0ef1b4e07d384	{"storage": "django.core.files.storage.FileSystemStorage", "name": "cache/96/c5/96c5c66feac2bd2ee38dbd0a1b900d5f.jpg", "size": [200, 62]}
sorl-thumbnail||thumbnails||f97b805222cce6260e2daf0649dc3a70	["de1a101b78064620e0a0ef1b4e07d384"]
sorl-thumbnail||image||e7c44eb080d9076e6b6e42271cf44b9f	{"storage": "django.core.files.storage.FileSystemStorage", "name": "uploads/images/service.PNG", "size": [1365, 253]}
sorl-thumbnail||image||d33915338bc1f1196b6582dc8d7b7012	{"storage": "django.core.files.storage.FileSystemStorage", "name": "cache/ec/2d/ec2dc3a6c064ae9fd6db9b8eaa60fefb.jpg", "size": [200, 37]}
sorl-thumbnail||thumbnails||e7c44eb080d9076e6b6e42271cf44b9f	["d33915338bc1f1196b6582dc8d7b7012"]
\.


--
-- Data for Name: web_aboutus; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY web_aboutus (dates_ptr_id, title, description) FROM stdin;
5	About Us	Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
\.


--
-- Data for Name: web_blog; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY web_blog (dates_ptr_id, title, description, author) FROM stdin;
34	Wanted Marketing Executives 	Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut 	suhad
35	Wanted Developers with 4 yrs experience	Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt 	Shajeer
36	Started our new office in kadavanthra	Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut 	Remya
\.


--
-- Data for Name: web_comment; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY web_comment (dates_ptr_id, blog_id_id, author, description) FROM stdin;
\.


--
-- Data for Name: web_contactus; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY web_contactus (dates_ptr_id, name, email_id, message) FROM stdin;
41	dvxdv	geethusureh@gmail.com	xccz
42	kjhh	geethusureh@gmail.com	jhhguhi
43	geethu	geethusureh@gmail.com	geethu
44	geeth	geethusureh@gmail.com	geethu suresh
45	geeth	geethusureh@gmail.com	geethu suresh
46	geethu suresh	geethusureh@gmail.com	test message to the admin
47	geethu suresh	geethusureh@gmail.com	sending the first test mail to the admin
48	geethu suresh	geethusureh@gmail.com	sending the first test mail to the admin
49	geeth	geethusureh@gmail.com	test
50	geethu	geethusureh@gmail.com	krishna 
51	malu	geethysuresh@gmail.com	geethu suresh
52	malu	geethysuresh@gmail.com	geethu suresh
53	geethu	geethusureh@gmail.com	geethu
54	geethu	geethusureh@gmail.com	geethu
55	geethu	geethusureh@gmail.com	geethy
56	geethu	geethusureh@gmail.com	geetu
57	gee	geethusureh@gmail.com	gee
58	krishna	knsureshlic@gmail.com	geethu
59	geeth	geethusureh@gmail.com	abc def ghi jkl mno pqr stu vwx yz
60	geeth	geethusureh@gmail.com	abc def ghi jkl mno pqr stu vwx yz
61	geethu	geethusureh@gmail.com	geethu
65	geethu	geethusureh@gmail.com	geethu
66	devu	geethusureh@gmail.com	devu
67	devu	geethusureh@gmail.com	devu
68	devu	geethusureh@gmail.com	devu
69	geethu suresh	geethusureh@gmail.com	test mail
70	geethu suresh	geethusureh@gmail.com	test mail
71	geethu suresh	sremya218@gmail.com	test mail
72	Remya 	sremya218@gmail.com	test mail
73	Remya 	sremya218@gmail.com	test mail
74	geethu Suresh	geethugate@gmail.com	Test mail
75	geethu Suresh	geethugate@gmail.com	Test mail
76	geethu Suresh	geethugate@gmail.com	Test mail
77	geethu Suresh	geethysuresh@gmail.com	Test mail
78	geethu Suresh	geethysuresh@gmail.com	Test mail
79	gqkhh	geethysuresh@gmail.com	mnbkbkjkhihjhuihi\nutfytftfwyfywfy\nuyguyfuywgdyuwguwgd
80	gqkhh	geethysuresh@gmail.com	mnbkbkjkhihjhuihi\nutfytftfwyfywfy\nuyguyfuywgdyuwguwgd
81	gqkhh	geethysuresh@gmail.com	mnbkbkjkhihjhuihi\nutfytftfwyfywfy\nuyguyfuywgdyuwguwgd
82	gqkhh	geethysuresh@gmail.com	mnbkbkjkhihjhuihi\nutfytftfwyfywfy\nuyguyfuywgdyuwguwgd
83	gqkhhhvcyc ytdrtrd	geethysuresh@gmail.com	mnbkbkjkhihjhuihi\nutfytftfwyfywfy\nuyguyfuywgdyuwguwgd
84	gqkhhhvcyc ytdrtrd	geethysuresh@gmail.com	mnbkbkjkhihjhuihi\nutfytftfwyfywfy\nuyguyfuywgdyuwguwgd
85	gqkhhhvcyc ytdrtrd	geethysuresh@gmail.com	mnbkbkjkhihjhuihi\nutfytftfwyfywfy\nuyguyfuywgdyuwguwgd
86	gqkhhhvcyc ytdrtrd	geethysuresh@gmail.com	mnbkbkjkhihjhuihi\nutfytftfwyfywfy\nuyguyfuywgdyuwguwgd
87	gqkhhhvcyc ytdrtrd	geethysuresh@gmail.com	mnbkbkjkhihjhuihi\nutfytftfwyfywfy\nuyguyfuywgdyuwguwgd
\.


--
-- Data for Name: web_dates; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY web_dates (id, created_date, modified_date) FROM stdin;
1	2013-07-20 21:27:49.730167+05:30	2013-07-20 21:27:49.73021+05:30
3	2013-07-20 21:35:46.36056+05:30	2013-07-20 21:35:46.360599+05:30
5	2013-07-20 21:42:07.882694+05:30	2013-07-20 21:42:07.882733+05:30
9	2013-07-22 12:08:03.895402+05:30	2013-07-22 12:08:03.895441+05:30
11	2013-07-23 13:47:14.887792+05:30	2013-07-23 13:47:14.887877+05:30
34	2013-07-27 15:37:55.279536+05:30	2013-07-27 16:21:13.724525+05:30
35	2013-07-27 15:38:39.983505+05:30	2013-07-27 16:21:23.856595+05:30
36	2013-07-27 15:39:28.481811+05:30	2013-07-27 16:21:40.420731+05:30
30	2013-07-26 14:14:47.668349+05:30	2013-07-29 16:54:21.605004+05:30
31	2013-07-26 14:14:47.676795+05:30	2013-07-29 16:54:21.617149+05:30
32	2013-07-26 14:14:47.682467+05:30	2013-07-29 16:54:21.624165+05:30
33	2013-07-26 14:14:47.687868+05:30	2013-07-29 16:54:21.631125+05:30
41	2013-07-30 14:19:11.132881+05:30	2013-07-30 14:19:11.132951+05:30
42	2013-07-30 14:26:36.128005+05:30	2013-07-30 14:26:36.128123+05:30
43	2013-07-30 14:32:21.941188+05:30	2013-07-30 14:32:21.941242+05:30
44	2013-07-30 14:47:05.383368+05:30	2013-07-30 14:47:05.383451+05:30
45	2013-07-30 14:49:03.560388+05:30	2013-07-30 14:49:03.560443+05:30
46	2013-07-30 14:52:56.072431+05:30	2013-07-30 14:52:56.072482+05:30
47	2013-07-30 14:54:15.443241+05:30	2013-07-30 14:54:15.443296+05:30
48	2013-07-30 14:56:29.690953+05:30	2013-07-30 14:56:29.691011+05:30
49	2013-07-30 14:57:49.607954+05:30	2013-07-30 14:57:49.608006+05:30
50	2013-07-30 14:59:34.124856+05:30	2013-07-30 14:59:34.124913+05:30
51	2013-07-30 15:01:39.888527+05:30	2013-07-30 15:01:39.888582+05:30
52	2013-07-30 15:12:18.439811+05:30	2013-07-30 15:12:18.439879+05:30
53	2013-07-30 15:26:16.387949+05:30	2013-07-30 15:26:16.388001+05:30
54	2013-07-30 15:36:21.31125+05:30	2013-07-30 15:36:21.311306+05:30
55	2013-07-30 15:48:24.84319+05:30	2013-07-30 15:48:24.84326+05:30
56	2013-07-30 15:50:38.321614+05:30	2013-07-30 15:50:38.32168+05:30
57	2013-07-30 15:55:13.644354+05:30	2013-07-30 15:55:13.644408+05:30
58	2013-07-30 16:07:33.122102+05:30	2013-07-30 16:07:33.122174+05:30
59	2013-07-30 16:26:06.163836+05:30	2013-07-30 16:26:06.163889+05:30
60	2013-07-30 16:26:28.61959+05:30	2013-07-30 16:26:28.619651+05:30
61	2013-07-30 17:48:45.402061+05:30	2013-07-30 17:48:45.402112+05:30
62	2013-07-30 17:54:09.876169+05:30	2013-07-30 17:54:09.876213+05:30
63	2013-07-30 17:54:53.171613+05:30	2013-07-30 17:54:53.171655+05:30
64	2013-07-30 17:55:19.028371+05:30	2013-07-30 17:55:19.028418+05:30
65	2013-07-31 14:34:51.108186+05:30	2013-07-31 14:34:51.108253+05:30
66	2013-07-31 14:50:31.679489+05:30	2013-07-31 14:50:31.679542+05:30
67	2013-07-31 14:51:20.469417+05:30	2013-07-31 14:51:20.469482+05:30
68	2013-07-31 14:53:39.407828+05:30	2013-07-31 14:53:39.407908+05:30
69	2013-07-31 15:06:09.672247+05:30	2013-07-31 15:06:09.672304+05:30
70	2013-07-31 15:06:09.999492+05:30	2013-07-31 15:06:09.999538+05:30
71	2013-07-31 15:16:36.341406+05:30	2013-07-31 15:16:36.341466+05:30
72	2013-07-31 15:18:09.988159+05:30	2013-07-31 15:18:09.988228+05:30
73	2013-07-31 15:19:30.760272+05:30	2013-07-31 15:19:30.76034+05:30
74	2013-08-01 14:06:04.067369+05:30	2013-08-01 14:06:04.067433+05:30
75	2013-08-01 14:13:23.788629+05:30	2013-08-01 14:13:23.788682+05:30
76	2013-08-01 14:13:38.557608+05:30	2013-08-01 14:13:38.557655+05:30
77	2013-08-01 14:14:05.77296+05:30	2013-08-01 14:14:05.773039+05:30
78	2013-08-01 14:14:05.787946+05:30	2013-08-01 14:14:05.787998+05:30
79	2013-08-01 14:15:33.352411+05:30	2013-08-01 14:15:33.352463+05:30
80	2013-08-01 14:17:23.37948+05:30	2013-08-01 14:17:23.37965+05:30
81	2013-08-01 14:18:18.278825+05:30	2013-08-01 14:18:18.278977+05:30
82	2013-08-01 14:18:23.501465+05:30	2013-08-01 14:18:23.501567+05:30
83	2013-08-01 14:21:15.591339+05:30	2013-08-01 14:21:15.591412+05:30
84	2013-08-01 16:30:36.393753+05:30	2013-08-01 16:30:36.393917+05:30
85	2013-08-01 16:31:28.85931+05:30	2013-08-01 16:31:28.85938+05:30
86	2013-08-01 16:47:06.161702+05:30	2013-08-01 16:47:06.161768+05:30
87	2013-08-01 16:47:34.757412+05:30	2013-08-01 16:47:34.757511+05:30
88	2013-09-20 13:17:23.500959+05:30	2013-09-20 13:17:23.501003+05:30
89	2013-09-20 13:17:23.531349+05:30	2013-09-20 13:17:23.531389+05:30
90	2013-09-20 13:17:23.564146+05:30	2013-09-20 13:17:23.564239+05:30
91	2013-09-20 13:18:06.730338+05:30	2013-09-20 13:18:06.730403+05:30
\.


--
-- Name: web_dates_id_seq; Type: SEQUENCE SET; Schema: public; Owner: geethu
--

SELECT pg_catalog.setval('web_dates_id_seq', 91, true);


--
-- Data for Name: web_feature; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY web_feature (dates_ptr_id, title, description, image) FROM stdin;
1	Website Feature	Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.	uploads/images/lap.jpg
\.


--
-- Data for Name: web_homepage; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY web_homepage (dates_ptr_id, logo, customer_care) FROM stdin;
9	uploads/images/logo.jpg	9539 000 975
91	uploads/images/logo.jpg	9539 000 975
\.


--
-- Data for Name: web_newsevents; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY web_newsevents (dates_ptr_id, title, description, event_date, image) FROM stdin;
11	News & Events	Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.	2013-07-23 13:47:11+05:30	
\.


--
-- Data for Name: web_services; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY web_services (dates_ptr_id, title, banner_image, content_subhead, description) FROM stdin;
62	\N	uploads/images/service.PNG	Custom Software Development	Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
\.


--
-- Data for Name: web_services_section; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY web_services_section (dates_ptr_id, section_head, section_image, description) FROM stdin;
63	Dedicated Staffing	uploads/images/dedicate.PNG	Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
64	Quality Assurance 	uploads/images/quality.PNG	Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
\.


--
-- Data for Name: web_slide; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY web_slide (dates_ptr_id, text, image, slideshow_id_id) FROM stdin;
31	<p id="first" >where technology</p><p id="second" > meets ecnomy</p>	uploads/images/banner.png	30
32	<p id="first" >where technology</p><p id="second" > meets ecnomy</p>	uploads/images/bannerr.jpg	30
33	<p id="first" >where technology</p><p id="second" > meets ecnomy</p>	uploads/images/banr.jpg	30
89	<p id="first" >where technology</p><p id="second" > meets ecnomy</p>	uploads/images/banner.png	88
90	<p id="first" >where technology</p><p id="second" > meets ecnomy</p>	uploads/images/banner_1.png	88
\.


--
-- Data for Name: web_slideshow; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY web_slideshow (dates_ptr_id, left_arrow, right_arrow, max_slide_count, bullet_active, bullet_inactive) FROM stdin;
30	uploads/images/leftArrow.png	uploads/images/rightArrow.png	3	uploads/images/redDot.png	uploads/images/whiteDot.png
88	uploads/images/leftArrow.png	uploads/images/rightArrow.png	3	uploads/images/redDot.png	uploads/images/whiteDot.png
\.


--
-- Data for Name: web_testimonials; Type: TABLE DATA; Schema: public; Owner: geethu
--

COPY web_testimonials (dates_ptr_id, title, description, image) FROM stdin;
3	Testimonials	Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.	uploads/images/TestimonialsBg.jpg
\.


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_model_key; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_key UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: south_migrationhistory_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY south_migrationhistory
    ADD CONSTRAINT south_migrationhistory_pkey PRIMARY KEY (id);


--
-- Name: thumbnail_kvstore_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY thumbnail_kvstore
    ADD CONSTRAINT thumbnail_kvstore_pkey PRIMARY KEY (key);


--
-- Name: web_aboutus_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY web_aboutus
    ADD CONSTRAINT web_aboutus_pkey PRIMARY KEY (dates_ptr_id);


--
-- Name: web_blog_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY web_blog
    ADD CONSTRAINT web_blog_pkey PRIMARY KEY (dates_ptr_id);


--
-- Name: web_comment_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY web_comment
    ADD CONSTRAINT web_comment_pkey PRIMARY KEY (dates_ptr_id);


--
-- Name: web_contactus_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY web_contactus
    ADD CONSTRAINT web_contactus_pkey PRIMARY KEY (dates_ptr_id);


--
-- Name: web_dates_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY web_dates
    ADD CONSTRAINT web_dates_pkey PRIMARY KEY (id);


--
-- Name: web_feature_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY web_feature
    ADD CONSTRAINT web_feature_pkey PRIMARY KEY (dates_ptr_id);


--
-- Name: web_homepage_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY web_homepage
    ADD CONSTRAINT web_homepage_pkey PRIMARY KEY (dates_ptr_id);


--
-- Name: web_newsevents_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY web_newsevents
    ADD CONSTRAINT web_newsevents_pkey PRIMARY KEY (dates_ptr_id);


--
-- Name: web_services_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY web_services
    ADD CONSTRAINT web_services_pkey PRIMARY KEY (dates_ptr_id);


--
-- Name: web_services_section_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY web_services_section
    ADD CONSTRAINT web_services_section_pkey PRIMARY KEY (dates_ptr_id);


--
-- Name: web_slide_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY web_slide
    ADD CONSTRAINT web_slide_pkey PRIMARY KEY (dates_ptr_id);


--
-- Name: web_slideshow_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY web_slideshow
    ADD CONSTRAINT web_slideshow_pkey PRIMARY KEY (dates_ptr_id);


--
-- Name: web_testimonials_pkey; Type: CONSTRAINT; Schema: public; Owner: geethu; Tablespace: 
--

ALTER TABLE ONLY web_testimonials
    ADD CONSTRAINT web_testimonials_pkey PRIMARY KEY (dates_ptr_id);


--
-- Name: auth_group_name_like; Type: INDEX; Schema: public; Owner: geethu; Tablespace: 
--

CREATE INDEX auth_group_name_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id; Type: INDEX; Schema: public; Owner: geethu; Tablespace: 
--

CREATE INDEX auth_group_permissions_group_id ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id; Type: INDEX; Schema: public; Owner: geethu; Tablespace: 
--

CREATE INDEX auth_group_permissions_permission_id ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id; Type: INDEX; Schema: public; Owner: geethu; Tablespace: 
--

CREATE INDEX auth_permission_content_type_id ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id; Type: INDEX; Schema: public; Owner: geethu; Tablespace: 
--

CREATE INDEX auth_user_groups_group_id ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id; Type: INDEX; Schema: public; Owner: geethu; Tablespace: 
--

CREATE INDEX auth_user_groups_user_id ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id; Type: INDEX; Schema: public; Owner: geethu; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_permission_id ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id; Type: INDEX; Schema: public; Owner: geethu; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_user_id ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_like; Type: INDEX; Schema: public; Owner: geethu; Tablespace: 
--

CREATE INDEX auth_user_username_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id; Type: INDEX; Schema: public; Owner: geethu; Tablespace: 
--

CREATE INDEX django_admin_log_content_type_id ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id; Type: INDEX; Schema: public; Owner: geethu; Tablespace: 
--

CREATE INDEX django_admin_log_user_id ON django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date; Type: INDEX; Schema: public; Owner: geethu; Tablespace: 
--

CREATE INDEX django_session_expire_date ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_like; Type: INDEX; Schema: public; Owner: geethu; Tablespace: 
--

CREATE INDEX django_session_session_key_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: thumbnail_kvstore_key_like; Type: INDEX; Schema: public; Owner: geethu; Tablespace: 
--

CREATE INDEX thumbnail_kvstore_key_like ON thumbnail_kvstore USING btree (key varchar_pattern_ops);


--
-- Name: web_comment_blog_id_id; Type: INDEX; Schema: public; Owner: geethu; Tablespace: 
--

CREATE INDEX web_comment_blog_id_id ON web_comment USING btree (blog_id_id);


--
-- Name: web_slide_slideshow_id_id; Type: INDEX; Schema: public; Owner: geethu; Tablespace: 
--

CREATE INDEX web_slide_slideshow_id_id ON web_slide USING btree (slideshow_id_id);


--
-- Name: auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: blog_id_id_refs_dates_ptr_id_7b20ac37994a8431; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY web_comment
    ADD CONSTRAINT blog_id_id_refs_dates_ptr_id_7b20ac37994a8431 FOREIGN KEY (blog_id_id) REFERENCES web_blog(dates_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: content_type_id_refs_id_d043b34a; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT content_type_id_refs_id_d043b34a FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dates_ptr_id_refs_id_208015549649b1df; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY web_blog
    ADD CONSTRAINT dates_ptr_id_refs_id_208015549649b1df FOREIGN KEY (dates_ptr_id) REFERENCES web_dates(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dates_ptr_id_refs_id_28bc44f2451549db; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY web_aboutus
    ADD CONSTRAINT dates_ptr_id_refs_id_28bc44f2451549db FOREIGN KEY (dates_ptr_id) REFERENCES web_dates(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dates_ptr_id_refs_id_36f157cbdb2e8602; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY web_slideshow
    ADD CONSTRAINT dates_ptr_id_refs_id_36f157cbdb2e8602 FOREIGN KEY (dates_ptr_id) REFERENCES web_dates(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dates_ptr_id_refs_id_3ab7fb35bd124261; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY web_services
    ADD CONSTRAINT dates_ptr_id_refs_id_3ab7fb35bd124261 FOREIGN KEY (dates_ptr_id) REFERENCES web_dates(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dates_ptr_id_refs_id_3eb1de10081b4273; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY web_slide
    ADD CONSTRAINT dates_ptr_id_refs_id_3eb1de10081b4273 FOREIGN KEY (dates_ptr_id) REFERENCES web_dates(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dates_ptr_id_refs_id_482d304109248435; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY web_comment
    ADD CONSTRAINT dates_ptr_id_refs_id_482d304109248435 FOREIGN KEY (dates_ptr_id) REFERENCES web_dates(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dates_ptr_id_refs_id_53ee9c8c5c5fdddd; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY web_homepage
    ADD CONSTRAINT dates_ptr_id_refs_id_53ee9c8c5c5fdddd FOREIGN KEY (dates_ptr_id) REFERENCES web_dates(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dates_ptr_id_refs_id_565ab729c711184a; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY web_feature
    ADD CONSTRAINT dates_ptr_id_refs_id_565ab729c711184a FOREIGN KEY (dates_ptr_id) REFERENCES web_dates(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dates_ptr_id_refs_id_6bcba043ea9baedd; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY web_newsevents
    ADD CONSTRAINT dates_ptr_id_refs_id_6bcba043ea9baedd FOREIGN KEY (dates_ptr_id) REFERENCES web_dates(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dates_ptr_id_refs_id_7044edb88e3a520f; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY web_services_section
    ADD CONSTRAINT dates_ptr_id_refs_id_7044edb88e3a520f FOREIGN KEY (dates_ptr_id) REFERENCES web_dates(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dates_ptr_id_refs_id_72b8a437dd23575e; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY web_contactus
    ADD CONSTRAINT dates_ptr_id_refs_id_72b8a437dd23575e FOREIGN KEY (dates_ptr_id) REFERENCES web_dates(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dates_ptr_id_refs_id_9a0d97f2ded3983; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY web_testimonials
    ADD CONSTRAINT dates_ptr_id_refs_id_9a0d97f2ded3983 FOREIGN KEY (dates_ptr_id) REFERENCES web_dates(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_id_refs_id_f4b32aac; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT group_id_refs_id_f4b32aac FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: slideshow_id_id_refs_dates_ptr_id_12f3c574d80e1aa4; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY web_slide
    ADD CONSTRAINT slideshow_id_id_refs_dates_ptr_id_12f3c574d80e1aa4 FOREIGN KEY (slideshow_id_id) REFERENCES web_slideshow(dates_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_40c41112; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT user_id_refs_id_40c41112 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_4dc23c39; Type: FK CONSTRAINT; Schema: public; Owner: geethu
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT user_id_refs_id_4dc23c39 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

