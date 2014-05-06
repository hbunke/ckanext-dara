#HB 2013-06-17


#XXX This is only a first very rough schema implementation.

#OrderedDict is not available in Python > 2.7
try:
    from collections import OrderedDict   # 2.7
except ImportError:
    #don't know which one's better...
    #from sqlalchemy.util import OrderedDict
    from ckanext.dara.ordered_dict import OrderedDict


class DaraField(object):
    """
    """

    def __init__(self, id, widget):

        self.id = id
        self.widget = widget


class DaraWidget(object):
    """
    """

    def __init__(self, form_type='input', name=u'', role=None, classes=[]):
        """
        """

        self.form_type = form_type
        self.name = name
        self.role = role
        self.classes = classes


class Input(DaraWidget):
    """
    """
    def __init__(self, size='', placeholder='', **kw):
        """
        """
        super(Input, self).__init__(**kw)
        self.size = size
        self.placeholder = placeholder


class Select(DaraWidget):
    """
    """

    def __init__(self, options, **kw):
        """
        """

        super(Select, self).__init__(**kw)
        self.form_type = 'select'
        self.options = options


class Text(DaraWidget):
    """
    """

    def __init__(self, placeholder='', **kw):
        """
        """
        super(Text, self).__init__(**kw)
        self.form_type = 'text'


class Date(DaraWidget):
    """
    """

    def __init__(self, **kw):
        """
        """
        super(Date, self).__init__(**kw)
        self.form_type = "date"


class DaraFields(object):
    """
    main class
    """

    def level_1(self):

        fields = [

            DaraField('PublicationDate',
                Input(
                    placeholder="eg. 2011",
                    name="Publication Year",
                    size='small',
                    classes=['dara_required']
                    )
                ),

            DaraField('Availabilitycontrolled',
                Select(
                    options=[
                        {'value': '1', 'text': 'Free Download'},
                        {'value': '2', 'text': 'Delivery on demand'},
                        {'value': '3', 'text': 'Onsite only'},
                        {'value': '4', 'text': 'Not available'},
                        {'value': '5', 'text': 'Unknown'},
                        ],
                    name = 'Availability (controlled)',
                    classes = ['dara_required']
                    ),
                ),
            
            DaraField('Availabilityfree',
                Input(
                    name = 'Availability (free)',
                    size = 'medium',
                    placeholder = 'eg. Die Datennutzung unterliegt schriftlichen Datenschutzvereinbarungen',
                    )
                )
            ]
        
        
        f = self.__transform(fields)

        schema = OrderedDict(f)
        return schema


    def level_2(self):
        """
        """
        fields = [
            
            DaraField('OtherTitle',
                Input(
                placeholder = 'eg. Subtitle, alternative title',
                role = 'master',
                name = 'Other Title',
                size = 'medium',
                )
            ),

            DaraField('OtherTitleType',
                    Select(
                    role = 'slave',
                    name = 'Type of other Title',
                    options = [
                        {'text': 'Alternative Title', 'value': '1'}, 
                        {'text': 'Translated Title', 'value': '2'}, 
                        {'text': 'Subtitle', 'value': '3'}, 
                        {'text': 'Original Title', 'value': '4'}],
                    )
            ),

            DaraField('currentVersion',
                    Input(
                    placeholder = 'eg. 1.1',
                    name = 'Version',
                    size = 'small',
                    )
            ),

            DaraField('language',
                    Select(
                    name = 'Language',
                    options = [
                        {'text': '', 'value': ''}, 
                        {'text': 'Belarusian', 'value': 'bel'}, 
                        {'text': 'Bosnian', 'value': 'bos'}, 
                        {'text': 'Czech', 'value': 'cze'}, 
                        {'text': 'Dutch', 'value': 'dut'}, 
                        {'text': 'English', 'value': 'eng'}, 
                        {'text': 'Estonian', 'value': 'est'}, 
                        {'text': 'Finnish', 'value': 'fin'}, 
                        {'text': 'French', 'value': 'fre'}, 
                        {'text': 'German', 'value': 'ger'}, 
                        {'text': 'Greek', 'value': 'gre'}, 
                        {'text': 'Croatian', 'value': 'hrv'}, 
                        {'text': 'Hungarian', 'value': 'hun'}, 
                        {'text': 'Italian', 'value': 'ita'}, 
                        {'text': 'Latvian', 'value': 'lav'}, 
                        {'text': 'Lithuanian', 'value': 'lit'}, 
                        {'text': 'Norwegian', 'value': 'nor'}, 
                        {'text': 'Polish', 'value': 'pol'}, 
                        {'text': 'Romanian', 'value': 'rum'}, 
                        {'text': 'Russian', 'value': 'rus'}, 
                        {'text': 'Slovak', 'value': 'slo'}, 
                        {'text': 'Slovenian', 'value': 'slv'}, 
                        {'text': 'Spanish', 'value': 'spa'}, 
                        {'text': 'Serbian', 'value': 'srp'}, 
                        {'text': 'Swedish', 'value': 'swe'}, 
                        {'text': 'Ukrainian', 'value': 'ukr'}],
                    )
            ),

            DaraField('AlternativeIdentifier_ID',
                    Input(
                    placeholder = 'eg. ISBN, Handle, DOI',
                    role = 'master',
                    name = 'Alternative Identifier',
                    )
            ),

            DaraField('AlternativeIdentifier_Type',
                    Select(
                    role = 'slave',
                    name = 'Type of Alternative Identifier',
                    options = [
                        {'text': ''}, 
                        {'text': 'DOI', 'value': 'DOI'}, 
                        {'text': 'ARK', 'value': 'ARK'}, 
                        {'text': 'EAN13', 'value': 'EAN13'}, 
                        {'text': 'EISSN', 'value': 'EISSN'}, 
                        {'text': 'Handle', 'value': 'Handle'}, 
                        {'text': 'ISBN', 'value': 'ISBN'}, 
                        {'text': 'ISSN', 'value': 'ISSN'}, 
                        {'text': 'ISTC', 'value': 'ISTC'}, 
                        {'text': 'LISSN', 'value': 'LISSN'}, 
                        {'text': 'LSID', 'value': 'LSID'}, 
                        {'text': 'PURL', 'value': 'PURL'}, 
                        {'text': 'UPC', 'value': 'UPC'}, 
                        {'text': 'URL', 'value': 'URL'}, 
                        {'text': 'URN', 'value': 'URN'}],
                    )
            ),

            DaraField('Universe_areaControlled',
                    Select(
                    classes = ['todo'],
                    name = 'Geographic Coverage (controlled)',
                    options = [{'text': ''}],
                    )
            ),

            DaraField('Universe_areaFree',
                    Input(
                    placeholder = 'eg. West-Germany',
                    name = 'Geographic Coverage (free)',
                    size = 'medium',
                    )
            ),

            DaraField('Universe_sampled',
                    Input(
                    placeholder = 'eg. adults in Eastern and Western Germany',
                    name = 'Sampled Universe',
                    size = 'medium',
                    )
            ),

            DaraField('SelectionMethod',
                    Text(
                    placeholder = 'Describe your selection method',
                    name = 'Sampling',
                    )
            ),

            DaraField('CollectionDate_controlled',
                    Date(
                    classes = ['todo'],
                    name = 'Collection Date (controlled)',
                    )
            ),

            DaraField('CollectionDate_free',
                    Input(
                    placeholder = 'eg. Spring 1999',
                    name = 'Collection Date (free)',
                    size = 'medium',
                    )
            ),

            DaraField('CollectionMode_controlled',
                    Select(
                    name = 'Collection Mode (controlled)',
                    options = [
                        {'text': '', 'value': ''}, 
                        {'text': 'Interview', 'value': '1'}, 
                        {'text': 'Interview: Face-to-Face', 'value': '2'}, 
                        {'text': 'Interview: Telephone', 'value': '3'}, 
                        {'text': 'Interview: E-Mail', 'value': '4'}, 
                        {'text': 'Interview: CATI', 'value': '5'}, 
                        {'text': 'Interview: CAPI', 'value': '6'}, 
                        {'text': 'Self-completed questionnaire', 'value': '7'}, 
                        {'text': 'Self-completed questionnaire: Paper/Pencil', 'value': '8'}, 
                        {'text': 'Self-completed questionnaire: Web-based', 'value': '9'}, 
                        {'text': 'Self-completed questionnaire: CASI', 'value': '10'}, 
                        {'text': 'Self-completed questionnaire: ACASI', 'value': '11'}, 
                        {'text': 'Coding', 'value': '12'}, {'text': 'Transcription', 'value': '13'}, 
                        {'text': 'Compilation', 'value': '14'}, 
                        {'text': 'Synthesis', 'value': '15'}, 
                        {'text': 'Recording', 'value': '16'}, 
                        {'text': 'Simulation', 'value': '17'}, 
                        {'text': 'Observation', 'value': '18'}, 
                        {'text': 'Observation: Field', 'value': '19'}, 
                        {'text': 'Observation: Laboratory', 'value': '20'}, 
                        {'text': 'Observation: Participant', 'value': '21'}, 
                        {'text': 'Experiments', 'value': '22'}, 
                        {'text': 'Focus Group', 'value': '23'}, 
                        {'text': 'Other', 'value': '24'}],
                    )
            ),

            DaraField('CollectionMode_free',
                    Input(
                    placeholder = 'eg. Interview',
                    name = 'Collection Mode (free)',
                    size = 'medium',
                    )
            ),

            DaraField('TimeDimension_controlled',
                    Select(
                    name = 'Time Dimension (controlled)',
                    options = [
                        {'text': '', 'value': ''}, 
                        {'text': 'Longitudinal ', 'value': '1'}, 
                        {'text': 'Longitudinal.CohortEventBased ', 'value': '2'}, 
                        {'text': 'Longitudinal.TrendRepeatedCrossSection ', 'value': '3'}, 
                        {'text': 'Longitudinal.Panel ', 'value': '4'}, 
                        {'text': 'Longitudinal.Panel.Continuous', 'value': '5'}, 
                        {'text': 'Longitudinal: Panel: Interval', 'value': '6'}, 
                        {'text': 'Time Series', 'value': '7'}, 
                        {'text': 'TimeSeries: Continuous', 'value': '8'}, 
                        {'text': 'TimeSeries: Discrete', 'value': '9'}, 
                        {'text': 'Cross-section', 'value': '10'}, 
                        {'text': 'Cross-section ad-hoc follow-up', 'value': '11'}, 
                        {'text': 'Other', 'value': '12'}],
                    )
            ),

            DaraField('TimeDimension_free',
                    Input(
                    placeholder = 'eg. Zeitreihe',
                    name = 'Time Dimension (free)',
                    size = 'medium',
                    )
            ),

            DaraField('DataCollector_name',
                    Input(
                    classes = ['todo'],
                    placeholder = 'eg. EMNID',
                    name = 'Data Collector',
                    )
            ),

            DaraField('Rights',
                    Input(
                    placeholder = 'eg. Copyright Joe Biggs',
                    name = 'Rights',
                    size = 'medium',
                    )
            ),

            DaraField('Note_text',
                    Text(
                    placeholder = 'any additional notes',
                    name = 'Notes',
                    )
            ),
        ]
            
        f = self.__transform(fields)

        schema = OrderedDict(f)
        return schema


    def level_3(self):
        """
        """
        
        fields = [
                
            DaraField('DataSet_dataType',
                Input(
                name = 'Type of Units',
                )
            ),

            DaraField('DataSet_numberUnits',
                Input(
                name = 'Number of Units',
                size = 'small',
                )
            ),

            DaraField('DataSet_numberVariables',
                Input(
                name = 'Number of Variables',
                size = 'small',
                )
            ),

            DaraField('DataSet_dataType',
                Input(
                name = 'Type of Data',
                )
            ),

            DaraField('File_format',
                Input(
                name = 'File Format',
                )
            ),

            DaraField('File_size',
                Input(
                name = 'Size',
                size = 'small',
                )
            ),

            DaraField('File_fingerprint',
                Input(
                role = 'master',
                name = 'Data Fingerprint',
                )
            ),

            DaraField('File_fingerprintMethod',
                Input(
                role = 'slave',
                name = 'Method Fingerprint',
                size = 'small',
                )
            ),
                
        ]

        f = self.__transform(fields)

        schema = OrderedDict(f)
        return schema


    def publication_fields(self):
        """
        """
        fields = [

            DaraField('Publication_Author',
                    Input(
                    name = 'Author of Publication',
                    size = 'medium',
                    )
            ),

            DaraField('Publication_Editor',
                    Input(
                    name = 'Editor',
                    size = 'medium',
                    )
            ),

            DaraField('Publication_Title',
                    Input(
                    name = 'Title of Publication',
                    size = 'medium',
                    )
            ),

            DaraField('Publication_Year',
                    Input(
                    name = 'Year of Publication',
                    )
            ),

            DaraField('Publication_Publisher',
                    Input(
                    name = 'Publisher',
                    size = 'medium',
                    )
            ),

            DaraField('Publication_PID',
                    Input(
                    role = 'master',
                    name = 'Persistent Identifier of Publication',
                    )
            ),

            DaraField('Publication_PIDType',
                    Select(
                    role = 'slave',
                    name = 'Type of Persistent Identifier',
                    options = [
                        {'text': '', 'value': ''}, 
                        {'text': 'DOI', 'value': 'DOI'}, 
                        {'text': 'ARK', 'value': 'ARK'}, 
                        {'text': 'EAN13', 'value': 'EAN13'}, 
                        {'text': 'EISSN', 'value': 'EISSN'}, 
                        {'text': 'Handle', 'value': 'Handle'}, 
                        {'text': 'ISBN', 'value': 'ISBN'}, 
                        {'text': 'ISSN', 'value': 'ISSN'}, 
                        {'text': 'ISTC', 'value': 'ISTC'}, 
                        {'text': 'LISSN', 'value': 'LISSN'}, 
                        {'text': 'LSID', 'value': 'LSID'}, 
                        {'text': 'PURL', 'value': 'PURL'}, 
                        {'text': 'UPC', 'value': 'UPC'}, 
                        {'text': 'URL', 'value': 'URL'}, 
                        {'text': 'URN', 'value': 'URN'}],
                    )
            ),

            DaraField('Publication_Place',
                    Input(
                    name = 'Place',
                    )
            ),

            DaraField('Publication_Journal',
                    Input(
                    name = 'Journal',
                    size = 'medium',
                    )
            ),

            DaraField('Publication_Volume',
                    Input(
                    name = 'Volume',
                    size = 'small',
                    )
            ),

            DaraField('Publication_Issue',
                    Input(
                    name = 'Issue',
                    size = 'small',
                    )
            ),

            DaraField('Publication_Anthology',
                    Input(
                    name = 'Anthology',
                    size = 'medium',
                    )
            ),

            DaraField('Publication_Pages',
                    Input(
                    name = 'Pages',
                    size = 'small',
                    )
            ),

            DaraField('Publication_ISBN',
                    Input(
                    name = 'ISBN',
                    size = 'small',
                    )
            ),

            DaraField('Publication_ISSN',
                    Input(
                    name = 'ISSN',
                    size = 'small',
                    )
            ),

            DaraField('Publication_RelationType',
                    Text(
                    name = 'Relation Type',
                    )
            ),

            DaraField('Publication_DocType',
                    Select(
                    name = 'Document Type',
                    options = [
                        {'text': '', 'value': ''}, 
                        {'text': 'Working Paper', 'value': '1'}, 
                        {'text': 'Article', 'value': '2'}, 
                        {'text': 'Report', 'value': '3'}, 
                        {'text': 'Book/Monograph', 'value': '4'}, 
                        {'text': 'Manuscript', 'value': '5'}, 
                        {'text': 'Reference Book', 'value': '6'}, 
                        {'text': 'Review', 'value': '7'}, 
                        {'text': 'Series', 'value': '8'}, 
                        {'text': 'Journal', 'value': '9'}, 
                        {'text': 'Magazine', 'value': '10'}],
                    )
            ),

        ]


        f = self.__transform(fields)

        schema = OrderedDict(f)
        return schema


    
    def level_all(self):
        """
        """
        level_1 = self.level_1()
        dara_all = level_1.copy()
        dara_all.update(self.level_2())
        dara_all.update(self.level_3())
        dara_all.update(self.publication_fields())
        return dara_all

    
    
    #TODO this should be temporary until we've refactored the templates
    def __transform(self, fields):
        """
        """
        f = []
        for field in fields:
            widget = field.widget
            id = field.id
            ft = (id, widget.__dict__)
            f.append(ft)
        return f

    



