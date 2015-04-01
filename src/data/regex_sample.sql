/*
IWM Document Repository, Document update script for the E-Service 13.2 Release
Created:    31/Dec/2012
Created by: Infosys Limited
Modified:   
Database:   Oracle 10g
Comments:   For updating PDF for RESP NASU Flow, it is assumed that this script 
			will run after a previous script adds the document to the DC_DOCUMENT table and 
			then initializes an empty_blob into the DC_REPOSITORY table.
*/
alter session set current_schema=IWM_COMMON;


SET SERVEROUTPUT ON FORMAT WRAPPED

DECLARE
   TYPE r_dc_repository IS RECORD (
       -- Represents the  unqique id assigned in the DC_DOCUMENT table.
       document_id     NUMBER(38),
       -- Represents the document file name.       
       document_name   VARCHAR(128),
       -- Represents the field mapping file name to update.
       field_mapping   VARCHAR(128)
   );

   TYPE dc_repository_table IS TABLE OF r_dc_repository
       INDEX BY BINARY_INTEGER;

   t_dc_repository dc_repository_table;

   v_file_loc           BFILE;
   v_document_loc       BLOB;
   v_field_mapping_loc  CLOB;
   v_document_size      INTEGER;
   
BEGIN
   -- Enter Documents and/or Field Mapping files to be loaded into DC_REPOSITORY table here.
   -- Enter null as Document or Field Mapping value to skip update for that attribute.
   
   -- RESP NASU SDE0069 English
   t_dc_repository(1).document_id := 220;
   t_dc_repository(1).document_name := 'SDE0069E.pdf';
   t_dc_repository(1).field_mapping := 'SDE0069E.xml';
   
   -- RESP NASU SDE0069 French
   t_dc_repository(2).document_id := 221;
   t_dc_repository(2).document_name := 'SDE0069F.pdf';
   t_dc_repository(2).field_mapping := 'SDE0069F.xml';
   
   -- RESP NASU SDE0071 English
   t_dc_repository(3).document_id := 222;
   t_dc_repository(3).document_name := 'SDE0071E.pdf';
   t_dc_repository(3).field_mapping := 'SDE0071E.xml';
   
   -- RESP NASU SDE0071 French
   t_dc_repository(4).document_id := 223;
   t_dc_repository(4).document_name := 'SDE0071F.pdf';
   t_dc_repository(4).field_mapping := 'SDE0071F.xml';
   
   -- RESP NASU SDE0073 English
   t_dc_repository(5).document_id := 224;
   t_dc_repository(5).document_name := 'SDE0073E.pdf';
   t_dc_repository(5).field_mapping := 'SDE0073E.xml';
   
   -- RESP NASU SDE0073 French
   t_dc_repository(6).document_id := 225;
   t_dc_repository(6).document_name := 'SDE0073F.pdf';
   t_dc_repository(6).field_mapping := 'SDE0073F.xml';
   
   -- RESP NASU ACES1 English
   t_dc_repository(7).document_id := 226;
   t_dc_repository(7).document_name := 'ACES1E.pdf';
   t_dc_repository(7).field_mapping := 'ACES1E.xml';
   
   -- RESP NASU ACES1 French
   t_dc_repository(8).document_id := 227;
   t_dc_repository(8).document_name := 'ACES1F.pdf';
   t_dc_repository(8).field_mapping := 'ACES1F.xml';
   
   -- RESP NASU SDE0088 English
   t_dc_repository(9).document_id := 228;
   t_dc_repository(9).document_name := 'SDE0088E.pdf';
   t_dc_repository(9).field_mapping := 'SDE0088E.xml';
   
   -- RESP NASU SDE0088 French
   t_dc_repository(10).document_id := 229;
   t_dc_repository(10).document_name := 'SDE0088F.pdf';
   t_dc_repository(10).field_mapping := 'SDE0088F.xml';
   
   -- RESP NASU SDE0089 English
   t_dc_repository(11).document_id := 230;
   t_dc_repository(11).document_name := 'SDE0089E.pdf';
   t_dc_repository(11).field_mapping := 'SDE0089E.xml';
   
   -- RESP NASU SDE0089 English
   t_dc_repository(12).document_id := 231;
   t_dc_repository(12).document_name := 'SDE0089F.pdf';
   t_dc_repository(12).field_mapping := 'SDE0089F.xml';
  
   -- End of dyanmic information update.
   
   -- Do not change anything beyond this point. 
      FOR i IN 1..t_dc_repository.COUNT LOOP
       DBMS_OUTPUT.PUT_LINE(CHR(0));
       DBMS_OUTPUT.PUT_LINE('Updating Document Id: [' || t_dc_repository(i).document_id || '] in the DC_REPOSITORY table...');

       IF t_dc_repository(i).document_name IS NOT NULL
       THEN
           DBMS_OUTPUT.PUT_LINE(CHR(0));
           DBMS_OUTPUT.PUT_LINE('Updating Document Name: [' || t_dc_repository(i).document_name || ']');
       
           v_file_loc := BFILENAME('BLOBDIR', t_dc_repository(i).document_name);
           v_document_size := DBMS_LOB.GETLENGTH(v_file_loc);

           DBMS_OUTPUT.PUT_LINE('Document size: ' || v_document_size);

           DBMS_OUTPUT.PUT('Updating existing document to empty blob...');

           UPDATE DC_REPOSITORY SET DOCUMENT=EMPTY_BLOB WHERE DOCUMENT_ID=t_dc_repository(i).document_id
            RETURNING DOCUMENT INTO v_document_loc;

           DBMS_OUTPUT.PUT_LINE(' done');
           
           DBMS_OUTPUT.PUT('Opening the document file...');
           DBMS_LOB.FILEOPEN( v_file_loc );
           DBMS_OUTPUT.PUT_LINE(' done');

           DBMS_OUTPUT.PUT('Loading Document From File...');
           DBMS_LOB.LOADFROMFILE(v_document_loc, v_file_loc, v_document_size);
           DBMS_OUTPUT.PUT_LINE(' done');

           DBMS_OUTPUT.PUT('Closing the document file...');
           DBMS_LOB.FILECLOSE( v_file_loc );
           DBMS_OUTPUT.PUT_LINE(' done');

       END IF;

       IF t_dc_repository(i).field_mapping IS NOT NULL
       THEN
           DBMS_OUTPUT.NEW_LINE;
           DBMS_OUTPUT.PUT_LINE('Updating Field Mapping for: [' || t_dc_repository(i).field_mapping || ']');
       
           v_file_loc := BFILENAME('BLOBDIR', t_dc_repository(i).field_mapping);
           v_document_size := DBMS_LOB.GETLENGTH(v_file_loc);

           DBMS_OUTPUT.PUT_LINE('Field Mapping file size: ' || v_document_size);

           DBMS_OUTPUT.PUT('Updating existing Field Mapping file to empty clob...');

           UPDATE DC_REPOSITORY SET FIELD_MAPPING=EMPTY_CLOB WHERE DOCUMENT_ID=t_dc_repository(i).document_id
            RETURNING FIELD_MAPPING INTO v_field_mapping_loc;

           DBMS_OUTPUT.PUT_LINE(' done');
           
           DBMS_OUTPUT.PUT('Opening the Field Mapping file...');
           DBMS_LOB.FILEOPEN( v_file_loc );
           DBMS_OUTPUT.PUT_LINE(' done');

           DBMS_OUTPUT.PUT('Loading Field Mapping From File...');
           DBMS_LOB.LOADFROMFILE(v_field_mapping_loc, v_file_loc, v_document_size);
           DBMS_OUTPUT.PUT_LINE(' done');

           DBMS_OUTPUT.PUT('Closing the Field Mapping file...');
           DBMS_LOB.FILECLOSE( v_file_loc );
           DBMS_OUTPUT.PUT_LINE(' done');
       END IF;

       -- Display a message when Document and Field Mapping variables are not defined.
       IF t_dc_repository(i).document_name IS NULL AND t_dc_repository(i).field_mapping IS NULL
       THEN
           DBMS_OUTPUT.PUT_LINE('Update not completed since Document and Field Mapping are not defined.');
       END IF;

   END LOOP;

   DBMS_OUTPUT.PUT_LINE(CHR(0));

   -- Commit the updates to the database.
   COMMIT;
   
EXCEPTION
   WHEN OTHERS
   THEN
      DBMS_OUTPUT.PUT_LINE('OTHERS Exception ' || sqlerrm);

END;
/