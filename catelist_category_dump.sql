--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.15
-- Dumped by pg_dump version 9.3.15
-- Started on 2016-12-09 23:45:00 +03

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 190 (class 1259 OID 25311)
-- Name: catelist_category; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE catelist_category (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    lft integer NOT NULL,
    rght integer NOT NULL,
    tree_id integer NOT NULL,
    level integer NOT NULL,
    parent_id integer,
    CONSTRAINT catelist_category_level_check CHECK ((level >= 0)),
    CONSTRAINT catelist_category_lft_check CHECK ((lft >= 0)),
    CONSTRAINT catelist_category_rght_check CHECK ((rght >= 0)),
    CONSTRAINT catelist_category_tree_id_check CHECK ((tree_id >= 0))
);


ALTER TABLE public.catelist_category OWNER TO postgres;

--
-- TOC entry 189 (class 1259 OID 25309)
-- Name: catelist_category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE catelist_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.catelist_category_id_seq OWNER TO postgres;

--
-- TOC entry 2041 (class 0 OID 0)
-- Dependencies: 189
-- Name: catelist_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE catelist_category_id_seq OWNED BY catelist_category.id;


--
-- TOC entry 1912 (class 2604 OID 25314)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY catelist_category ALTER COLUMN id SET DEFAULT nextval('catelist_category_id_seq'::regclass);


--
-- TOC entry 2036 (class 0 OID 25311)
-- Dependencies: 190
-- Data for Name: catelist_category; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY catelist_category (id, name, lft, rght, tree_id, level, parent_id) FROM stdin;
1	Scholl	1	6	2	0	\N
4	Teacher	4	5	2	1	1
5	Pupil	2	3	2	1	1
6	Professor	2	3	3	1	2
2	University	1	6	3	0	\N
7	Student	4	5	3	1	2
8	Colonel	2	3	1	1	3
3	Army	1	6	1	0	\N
9	Soldier	4	5	1	1	3
\.


--
-- TOC entry 2042 (class 0 OID 0)
-- Dependencies: 189
-- Name: catelist_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('catelist_category_id_seq', 9, true);


--
-- TOC entry 1924 (class 2606 OID 25322)
-- Name: catelist_category_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY catelist_category
    ADD CONSTRAINT catelist_category_name_key UNIQUE (name);


--
-- TOC entry 1926 (class 2606 OID 25320)
-- Name: catelist_category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY catelist_category
    ADD CONSTRAINT catelist_category_pkey PRIMARY KEY (id);


--
-- TOC entry 1917 (class 1259 OID 25329)
-- Name: catelist_category_3cfbd988; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX catelist_category_3cfbd988 ON catelist_category USING btree (rght);


--
-- TOC entry 1918 (class 1259 OID 25330)
-- Name: catelist_category_656442a0; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX catelist_category_656442a0 ON catelist_category USING btree (tree_id);


--
-- TOC entry 1919 (class 1259 OID 25332)
-- Name: catelist_category_6be37982; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX catelist_category_6be37982 ON catelist_category USING btree (parent_id);


--
-- TOC entry 1920 (class 1259 OID 25331)
-- Name: catelist_category_c9e9a848; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX catelist_category_c9e9a848 ON catelist_category USING btree (level);


--
-- TOC entry 1921 (class 1259 OID 25328)
-- Name: catelist_category_caf7cc51; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX catelist_category_caf7cc51 ON catelist_category USING btree (lft);


--
-- TOC entry 1922 (class 1259 OID 25333)
-- Name: catelist_category_name_b3574bee_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX catelist_category_name_b3574bee_like ON catelist_category USING btree (name varchar_pattern_ops);


--
-- TOC entry 1927 (class 2606 OID 25323)
-- Name: catelist_category_parent_id_384917eb_fk_catelist_category_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY catelist_category
    ADD CONSTRAINT catelist_category_parent_id_384917eb_fk_catelist_category_id FOREIGN KEY (parent_id) REFERENCES catelist_category(id) DEFERRABLE INITIALLY DEFERRED;


-- Completed on 2016-12-09 23:45:00 +03

--
-- PostgreSQL database dump complete
--

