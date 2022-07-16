import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0001_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0001   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '市民１'),
    TXT(0x02, '喵呜'),
    TXT(0x03, '地图物体0'),
    TXT(0x04, '宝箱'),
    TXT(0x05, '宝箱'),
    TXT(0x06, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'map1'
    header.mapModel       = 'T0001.x'
    header.mapIndex       = 1
    header.bgm            = 0
    header.flags          = 0x0000
    header.entryFunction  = 0x0010
    header.importTable    = ['ED6_DT01/T0001._SN', 'ED6_DT01/T0001_1._SN', 'ED6_DT01/T0001_2._SN', 'ED6_DT01/T0001_3._SN', 'ED6_DT01/T0001_4._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x113C
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00000000,
            word_0C         = 0x0004,
            word_0E         = 0x0005,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 2500,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 1,
            word_3A         = 1,
            preInitScena    = 0x0000,
            preInitFunction = 0x0001,
            initScena       = 0x0000,
            initFunction    = 0x0002,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT09/CH10000._CH', 'ED6_DT09/CH10000P._CP'),
        ('ED6_DT09/CH10001._CH', 'ED6_DT09/CH10001P._CP'),
    ]

# id: 0x10002 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = -4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0001,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -4000,
            z                   = 0,
            y                   = -2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0001,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0100,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -4000,
            z                   = 0,
            y                   = -4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0000,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -5000,
            z                   = 0,
            y                   = -6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0000,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x162
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 10000,
            z           = 0,
            y           = -4000,
            word_0C     = 0x0000,
            word_0E     = 0x0001,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x07D0,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x17E
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 10000,
            y           = 0,
            z           = -1000,
            range       = 11000,
            dword_10    = 0x000003E8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000B,
        ),
    )

# id: 0x10005 offset: 0x19E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -2000,
            triggerZ            = 1000,
            triggerY            = 0,
            triggerRange        = 1000,
            actorX              = -2000,
            actorZ              = 1000,
            actorY              = 0,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -18000,
            triggerZ            = 1000,
            triggerY            = 18000,
            triggerRange        = 1000,
            actorX              = -2000,
            actorZ              = 1000,
            actorY              = 0,
            flags               = 0x007E,
            talkScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1E6
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x1E7
@scena.Code('Init')
def Init():
    ClearScenaFlags(ScenaFlag(0x0043, 6, 0x21E))
    Event(0, 0x000B)
    OP_62(0x0009, 0xFFFFFDA8, 300, 0x80, 0x21, 0x000000FA, 0x00)
    SetChrFlags(0x0009, 0x0006)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrPos(0x0009, -4000, 1000, -2000, 0)

    ExecExpressionWithValue(
        0x0009,
        0x2A,
        (
            (Expr.PushLong, 0x7530),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x2B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x2C,
        (
            (Expr.PushLong, 0x15F90),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x2D,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x2E,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x2F,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0043, 1, 0x219)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5C3',
    )

    SetScenaFlags(ScenaFlag(0x0043, 1, 0x219))
    FormationDelMember(0x00, 0xFF)
    FormationAddMember(0x01, 0x00)
    FormationAddMember(0x00, 0x01)
    FormationAddMember(0x05, 0x02)
    FormationAddMember(0x07, 0x03)
    SetChrStatus(0x0003, 0x00, 3)
    SetChrStatus(0x0004, 0x00, 3)
    SetChrStatus(0x0006, 0x00, 3)
    SetChrStatus(0x0002, 0x00, 3)
    SetChrStatus(0x0000, 0x07, 4)
    SetChrStatus(0x0000, 0x00, 3)
    SetChrStatus(0x0001, 0x07, 3)
    SetChrStatus(0x0001, 0x00, 3)
    SetChrStatus(0x0000, 0x07, 3)
    OP_34(0x00, 0x006E)
    OP_34(0x00, 0x006F)
    OP_34(0x00, 0x0074)
    OP_34(0x00, 0x0076)
    OP_34(0x00, 0x000A)
    OP_34(0x00, 0x000B)
    OP_34(0x00, 0x000D)
    OP_34(0x00, 0x0010)
    OP_34(0x00, 0x0014)
    OP_34(0x00, 0x0018)
    OP_34(0x00, 0x0032)
    OP_34(0x00, 0x0033)
    OP_34(0x00, 0x0034)
    OP_34(0x00, 0x0036)
    OP_34(0x00, 0x003E)
    OP_34(0x00, 0x003F)
    OP_34(0x00, 0x004B)
    OP_34(0x00, 0x004C)
    OP_34(0x00, 0x0050)
    OP_34(0x00, 0x0064)
    OP_34(0x00, 0x0069)
    OP_34(0x01, 0x006E)
    OP_34(0x01, 0x006F)
    OP_34(0x01, 0x0070)
    OP_34(0x01, 0x000A)
    OP_34(0x01, 0x000C)
    OP_34(0x01, 0x000D)
    OP_34(0x01, 0x0014)
    OP_34(0x01, 0x0015)
    OP_34(0x01, 0x0017)
    OP_34(0x01, 0x0032)
    OP_34(0x01, 0x0033)
    OP_34(0x01, 0x0034)
    OP_34(0x01, 0x0036)
    OP_34(0x01, 0x0037)
    OP_34(0x01, 0x003C)
    OP_34(0x01, 0x003E)
    OP_34(0x01, 0x003F)
    OP_34(0x01, 0x004B)
    OP_34(0x01, 0x004C)
    OP_34(0x01, 0x0050)
    OP_34(0x01, 0x0064)
    OP_34(0x01, 0x0069)
    OP_34(0x02, 0x0078)
    OP_34(0x03, 0x0078)
    AddCraft(0x0000, 0x0096)
    AddCraft(0x0000, 0x0097)
    AddCraft(0x0000, 0x0098)
    AddCraft(0x0000, 0x0099)
    AddCraft(0x0000, 0x009A)
    AddCraft(0x0001, 0x00A0)
    AddCraft(0x0001, 0x00A1)
    AddCraft(0x0001, 0x00A2)
    AddCraft(0x0001, 0x00A3)
    AddCraft(0x0001, 0x00A4)
    AddCraft(0x0002, 0x00AA)
    AddCraft(0x0002, 0x00AB)
    AddCraft(0x0002, 0x00AC)
    AddCraft(0x0003, 0x00B4)
    AddCraft(0x0003, 0x00B5)
    AddCraft(0x0003, 0x00B6)
    AddCraft(0x0004, 0x00BE)
    AddCraft(0x0004, 0x00BF)
    AddCraft(0x0005, 0x00C8)
    AddCraft(0x0005, 0x00C9)
    AddCraft(0x0005, 0x00CA)
    AddCraft(0x0005, 0x00CB)
    AddCraft(0x0006, 0x00D2)
    AddCraft(0x0006, 0x00D3)
    AddCraft(0x0007, 0x00DD)
    AddCraft(0x0007, 0x00DE)
    AddCraft(0x0007, 0x00DC)
    AddSCraft(0x0000, 0x00E6)
    AddSCraft(0x0000, 0x00E7)
    AddSCraft(0x0001, 0x00EB)
    AddSCraft(0x0001, 0x00EC)
    AddSCraft(0x0002, 0x00F0)
    AddSCraft(0x0003, 0x00F5)
    AddSCraft(0x0004, 0x00FA)
    AddSCraft(0x0005, 0x00FF)
    AddSCraft(0x0005, 0x0100)
    AddSCraft(0x0006, 0x0104)
    AddSCraft(0x0007, 0x0109)
    AddSCraft(0x0007, 0x010A)
    EquipCmd(0x00, 0x0001)
    EquipCmd(0x01, 0x001F)
    EquipCmd(0x05, 0x0097)
    EquipCmd(0x02, 0x003D)
    EquipCmd(0x04, 0x0079)
    EquipCmd(0x06, 0x00B5)
    EquipCmd(0x03, 0x005B)
    EquipCmd(0x07, 0x03E8)
    AddSepith(0x00, 20)
    AddSepith(0x01, 20)
    AddSepith(0x02, 20)
    AddSepith(0x03, 20)
    OP_37(0x00, 0x0000)
    OP_37(0x01, 0x0000)
    AddItem(0x0258, 1)
    AddItem(0x0259, 1)
    AddItem(0x025E, 1)
    EquipCmd(0x00, 0x00F1)
    EquipCmd(0x01, 0x00F1)
    EquipCmd(0x00, 0x010F)
    EquipCmd(0x01, 0x010F)
    AddItem(0x01F5, 50)
    AddItem(0x012D, 2)
    AddItem(0x012E, 2)
    AddItem(0x012F, 2)
    AddItem(0x0130, 2)
    AddItem(0x0131, 2)
    AddItem(0x0132, 2)
    AddItem(0x0133, 2)
    AddItem(0x0134, 2)
    AddItem(0x0135, 2)
    AddItem(0x0136, 2)
    AddItem(0x0137, 2)
    AddItem(0x0138, 2)
    AddItem(0x0139, 2)
    AddItem(0x013A, 2)
    AddItem(0x013B, 2)
    AddItem(0x013C, 2)
    AddItem(0x013D, 2)
    AddItem(0x013E, 2)
    AddItem(0x013F, 2)
    AddItem(0x0140, 2)
    AddItem(0x0141, 2)
    AddItem(0x0142, 2)
    AddItem(0x0143, 2)
    AddItem(0x0144, 2)
    AddItem(0x0145, 2)
    AddItem(0x0146, 2)
    AddItem(0x0147, 2)
    AddItem(0x0258, 4)
    AddItem(0x025B, 4)
    AddItem(0x025E, 4)
    AddItem(0x0261, 4)
    AddItem(0x0264, 4)
    AddItem(0x0267, 4)
    AddItem(0x026A, 4)
    AddItem(0x026D, 4)
    AddItem(0x0270, 4)
    AddItem(0x0273, 4)
    AddItem(0x0276, 4)
    AddItem(0x0279, 1)
    AddItem(0x027A, 1)
    AddItem(0x027B, 1)
    AddItem(0x027C, 1)
    AddItem(0x0285, 1)
    AddItem(0x0286, 1)
    AddItem(0x0287, 1)
    AddItem(0x027D, 1)
    AddItem(0x027E, 1)
    AddItem(0x027F, 1)
    AddItem(0x0280, 1)
    AddItem(0x0281, 1)
    AddItem(0x0282, 1)
    AddItem(0x0283, 1)
    AddItem(0x028A, 2)
    AddItem(0x028B, 2)
    AddItem(0x028D, 4)
    AddItem(0x0294, 4)
    AddItem(0x0296, 4)
    AddItem(0x02B2, 4)
    AddItem(0x02BC, 2)
    AddItem(0x02BD, 2)
    AddItem(0x02BE, 2)
    AddItem(0x02C6, 2)
    AddItem(0x02C8, 2)
    AddItem(0x02C1, 2)
    AddItem(0x028C, 2)
    AddItem(0x0291, 2)
    AddItem(0x02D0, 1)
    AddItem(0x02D1, 1)
    AddItem(0x02D2, 1)
    AddItem(0x02D3, 1)
    AddItem(0x02D4, 1)
    SetMapFlags(0x01000000)
    SetMapFlags(0x00800000)

    def _loc_5C3(): pass

    label('loc_5C3')

    SetMapFlags(0x00000001)
    ClearMapFlags(0x00000020)
    ClearMapFlags(0x00400000)

    Return()

# id: 0x0002 offset: 0x5D3
@scena.Code('ReInit')
def ReInit():
    Return()

# id: 0x0003 offset: 0x5D4
@scena.Code('func_03_5D4')
def func_03_5D4():
    SetChrPos(0x000C, 2000, 0, 2000, 0)
    OP_A1(0x000C, 0x0006)
    Sleep(1)

    SetChrBattleFlags(0x0008, 0x0020)
    OP_89(0x0008, 2000, 2000, 2000, 0)
    Sleep(3000)

    ChrMoveTo(0x000C, 4000, 1000, 2000, 2000, 0x00)

    Return()

# id: 0x0004 offset: 0x61F
@scena.Code('func_04_61F')
def func_04_61F():
    Return()

# id: 0x0005 offset: 0x620
@scena.Code('func_05_620')
def func_05_620():
    Call(0, 0x000B)

    Return()

# id: 0x0006 offset: 0x625
@scena.Code('func_06_625')
def func_06_625():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_647',
    )

    ChrTalk(
        0x00FE,
        (
            '设立local flag哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_647(): pass

    label('loc_647')

    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))
    SetMessageWindowPos(100, 100, 15, 2)

    Talk(
        (
            '#200W可以指定坐标显示哦。',
            TxtCtl.Enter,
            '\n',
            '#W是真的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '#20A等两秒～',
            TxtCtl.Enter,
            '#A如果不指定坐标，\n',
            '就会在画面中央显示哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            '请指定恢复时的默认坐标。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x00FE,
        (
            '#010F#1P靠近左上',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#010F#2P靠近右上',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#010F#3P靠近左下',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#010F#4P靠近右下',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#010F#5P靠近上方',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#010F#6P靠近下方',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你知道吗？按下F11，\n',
            '就可以看到事件区域了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#010F我啊，和爱娜！结婚了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0001,
        (
            '#020F哦哦？哈～哈哈哈哈哈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0001,
        (
            '#020F没想到在这里见到\n',
            '爱娜朝思暮想的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrName('约修亚')

    Talk(
        (
            '#000F暑假已经结束了。',
            TxtCtl.Enter,
            '\n',
            '#4Sあああああ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_61(0x0101)

    Talk(
        (
            '#F#2Sあいうえお#10R a   i   u   e   o#',
            TxtCtl.Enter,
            '\n',
            'かきくけこ#10R ka  ki  ku  ke  ko#さしすせそ#10R sa  si  su  se  so#\n',
            '真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x8C2
@scena.Code('func_07_8C2')
def func_07_8C2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8E6',
    )

    OP_8D(0x00FE, 5000, -5000, 15000, 9000, 2000)
    Yield()

    Jump('func_07_8C2')

    def _loc_8E6(): pass

    label('loc_8E6')

    Return()

# id: 0x0008 offset: 0x8E7
@scena.Code('func_08_8E7')
def func_08_8E7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_922',
    )

    OP_70(0x0001, 50)
    OP_8D(0x00FE, -10000, -10000, 1000, 1000, 2000)
    OP_6F(0x0001, 0)
    OP_72(0x0001, 0x0008)
    Sleep(2000)

    Jump('func_08_8E7')

    def _loc_922(): pass

    label('loc_922')

    Return()

# id: 0x0009 offset: 0x923
@scena.Code('func_09_923')
def func_09_923():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_937',
    )

    SetChrDirection(0x00FE, 180, 5000)
    Yield()

    Jump('func_09_923')

    def _loc_937(): pass

    label('loc_937')

    Return()

# id: 0x000A offset: 0x938
@scena.Code('func_0A_938')
def func_0A_938():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_95B',
    )

    OP_8D(0x0000, 10000, 10000, -10000, -10000, 2000)

    Jump('func_0A_938')

    def _loc_95B(): pass

    label('loc_95B')

    Return()

# id: 0x000B offset: 0x95C
@scena.Code('func_0B_95C')
def func_0B_95C():
    OP_16(0x01)
    EventBegin(0x00)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrName('跳转君')

    Talk(
        (
            '请选择地图。',
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_98A(): pass

    label('loc_98A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B91',
    )

    Menu(
        0,
        10,
        10,
        1,
        (
            TXT(0x00, '测试地图\n'),
            TXT(0x01, '游戏地图\n'),
            TXT(0x02, '角色一览\n'),
            TXT(0x03, '魔兽一览\n'),
            TXT(0x04, '地图对象一览\n'),
            TXT(0x05, '战斗\n'),
            TXT(0x06, '战斗（魔兽计算测试）\n'),
            TXT(0x07, '战斗（确认地图）\n'),
            TXT(0x08, '战斗（检测用）\n'),
            TXT(0x09, '事件列表\n'),
            TXT(0x0A, '商店测试\n'),
            TXT(0x0B, '存档菜单\n'),
            TXT(0x0C, '绝对模式视角测试\n'),
            TXT(0x0D, '返回标题画面\n'),
            TXT(0x0E, '影像播放·停止\n'),
            TXT(0x0F, '取消\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_16(0x01)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_AA6'),
        (0x00000001, 'loc_AAD'),
        (0x00000002, 'loc_AB4'),
        (0x00000003, 'loc_ABB'),
        (0x00000004, 'loc_AC2'),
        (0x00000005, 'loc_AC9'),
        (0x00000006, 'loc_AD0'),
        (0x00000007, 'loc_AD7'),
        (0x00000008, 'loc_ADE'),
        (0x00000009, 'loc_AE5'),
        (0x0000000A, 'loc_AEC'),
        (0x0000000B, 'loc_AF8'),
        (0x0000000C, 'loc_AFC'),
        (0x0000000D, 'loc_B00'),
        (0x0000000E, 'loc_B5B'),
        (0x0000000F, 'loc_B60'),
        (-1, 'loc_B81'),
    )

    def _loc_AA6(): pass

    label('loc_AA6')

    Call(0, 0x000C)

    Jump('loc_B8E')

    def _loc_AAD(): pass

    label('loc_AAD')

    Call(3, 0x0002)

    Jump('loc_B8E')

    def _loc_AB4(): pass

    label('loc_AB4')

    Call(3, 0x0000)

    Jump('loc_B8E')

    def _loc_ABB(): pass

    label('loc_ABB')

    Call(3, 0x0001)

    Jump('loc_B8E')

    def _loc_AC2(): pass

    label('loc_AC2')

    Call(0, 0x000D)

    Jump('loc_B8E')

    def _loc_AC9(): pass

    label('loc_AC9')

    Call(0, 0x0011)

    Jump('loc_B8E')

    def _loc_AD0(): pass

    label('loc_AD0')

    Call(1, 0x0000)

    Jump('loc_B8E')

    def _loc_AD7(): pass

    label('loc_AD7')

    Call(2, 0x0000)

    Jump('loc_B8E')

    def _loc_ADE(): pass

    label('loc_ADE')

    Call(2, 0x002F)

    Jump('loc_B8E')

    def _loc_AE5(): pass

    label('loc_AE5')

    Call(4, 0x0000)

    Jump('loc_B8E')

    def _loc_AEC(): pass

    label('loc_AEC')

    OP_5F(0x0000)
    OP_56(0x00)
    Call(0, 0x0013)

    Jump('loc_B8E')

    def _loc_AF8(): pass

    label('loc_AF8')

    ShowSaveMenu()

    Jump('loc_B8E')

    def _loc_AFC(): pass

    label('loc_AFC')

    SaveClearData()

    Jump('loc_B8E')

    def _loc_B00(): pass

    label('loc_B00')

    OP_5F(0x0000)
    OP_56(0x00)
    Sleep(500)

    ClearMapFlags(0x00000001)
    OP_66(0x0000)
    OP_67(-15000, 10000, -10000, 1000)
    OP_69(0x0008, 1000)
    OP_69(0x0000, 1000)
    OP_66(0x0001)
    OP_67(0, 8000, -10000, 1000)
    OP_6C(45000, 1000)
    SetMapFlags(0x00000001)
    Sleep(500)

    Jump('loc_B8E')

    def _loc_B5B(): pass

    label('loc_B5B')

    OP_B4(0x00)

    Jump('loc_B8E')

    def _loc_B60(): pass

    label('loc_B60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Return,
        ),
        'loc_B70',
    )

    PlayMovie(0x01, '')
    ClearScenaFlags(ScenaFlag(0x0002, 5, 0x15))

    Jump('loc_B7E')

    def _loc_B70(): pass

    label('loc_B70')

    PlayMovie(0x00, 'logo.avi')
    SetScenaFlags(ScenaFlag(0x0002, 5, 0x15))

    def _loc_B7E(): pass

    label('loc_B7E')

    Jump('loc_B8E')

    def _loc_B81(): pass

    label('loc_B81')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_B8E')

    def _loc_B8E(): pass

    label('loc_B8E')

    Jump('loc_98A')

    def _loc_B91(): pass

    label('loc_B91')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    Sleep(300)

    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0xBA7
@scena.Code('func_0C_BA7')
def func_0C_BA7():
    Talk(
        (
            TxtCtl.ShowAll,
            '请选择测试地图。',
            TxtCtl.Enter,
        ),
    )

    def _loc_BBB(): pass

    label('loc_BBB')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CAF',
    )

    Menu(
        1,
        10,
        100,
        1,
        (
            TXT(0x00, '测试地图20\n'),
            TXT(0x01, '测试地图21\n'),
            TXT(0x02, '测试地图22\n'),
            TXT(0x03, '测试地图23\n'),
            TXT(0x04, '测试地图24\n'),
            TXT(0x05, '测试地图25\n'),
            TXT(0x06, '测试地图26\n'),
            TXT(0x07, '测试地图27\n'),
            TXT(0x08, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_C5A'),
        (0x00000001, 'loc_C63'),
        (0x00000002, 'loc_C6C'),
        (0x00000003, 'loc_C75'),
        (0x00000004, 'loc_C7E'),
        (0x00000005, 'loc_C87'),
        (0x00000006, 'loc_C90'),
        (0x00000007, 'loc_C99'),
        (-1, 'loc_CA2'),
    )

    def _loc_C5A(): pass

    label('loc_C5A')

    NewScene('ED6_DT01/T0020._SN', 0, 0, 0)
    IdleLoop()

    def _loc_C63(): pass

    label('loc_C63')

    NewScene('ED6_DT01/T0021._SN', 0, 0, 0)
    IdleLoop()

    def _loc_C6C(): pass

    label('loc_C6C')

    NewScene('ED6_DT01/T0022._SN', 0, 0, 0)
    IdleLoop()

    def _loc_C75(): pass

    label('loc_C75')

    NewScene('ED6_DT01/T0023._SN', 0, 0, 0)
    IdleLoop()

    def _loc_C7E(): pass

    label('loc_C7E')

    NewScene('ED6_DT01/T0024._SN', 0, 0, 0)
    IdleLoop()

    def _loc_C87(): pass

    label('loc_C87')

    NewScene('ED6_DT01/T0025._SN', 0, 0, 0)
    IdleLoop()

    def _loc_C90(): pass

    label('loc_C90')

    NewScene('ED6_DT01/T0026._SN', 0, 0, 0)
    IdleLoop()

    def _loc_C99(): pass

    label('loc_C99')

    NewScene('ED6_DT01/T0027._SN', 0, 0, 0)
    IdleLoop()

    def _loc_CA2(): pass

    label('loc_CA2')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_BBB')

    def _loc_CAF(): pass

    label('loc_CAF')

    OP_5F(0x0001)
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000D offset: 0xCBF
@scena.Code('func_0D_CBF')
def func_0D_CBF():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪个？',
            TxtCtl.Enter,
        ),
    )

    def _loc_CC9(): pass

    label('loc_CC9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D2D',
    )

    Menu(
        1,
        10,
        100,
        1,
        (
            TXT(0x00, '地图对象１\n'),
            TXT(0x01, '地图对象２\n'),
            TXT(0x02, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_D0E'),
        (0x00000001, 'loc_D17'),
        (-1, 'loc_D20'),
    )

    def _loc_D0E(): pass

    label('loc_D0E')

    NewScene('ED6_DT01/T0070._SN', 0, 0, 0)
    IdleLoop()

    def _loc_D17(): pass

    label('loc_D17')

    NewScene('ED6_DT01/T0071._SN', 0, 0, 0)
    IdleLoop()

    def _loc_D20(): pass

    label('loc_D20')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_CC9')

    def _loc_D2D(): pass

    label('loc_D2D')

    OP_5F(0x0001)
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000E offset: 0xD3D
@scena.Code('func_0E_D3D')
def func_0E_D3D():
    CameraSetDistance(5000, 3000)
    Call(0, 0x000F)

    Return()

# id: 0x000F offset: 0xD4B
@scena.Code('func_0F_D4B')
def func_0F_D4B():
    OP_6C(0, 20000)

    Return()

# id: 0x0010 offset: 0xD55
@scena.Code('func_10_D55')
def func_10_D55():
    EventBegin(0x00)
    OP_62(0x0000, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)

    Return()

# id: 0x0011 offset: 0xD6F
@scena.Code('func_11_D6F')
def func_11_D6F():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FBF',
    )

    Menu(
        1,
        10,
        100,
        1,
        (
            TXT(0x00, '测试\n'),
            TXT(0x01, '对角测试\n'),
            TXT(0x02, '直线攻击测试\n'),
            TXT(0x03, '测试地图2\n'),
            TXT(0x04, '10000-10070\n'),
            TXT(0x05, '10080-10150\n'),
            TXT(0x06, '10160-10220\n'),
            TXT(0x07, '00260-00330\n'),
            TXT(0x08, '00340-00410\n'),
            TXT(0x09, '最终BOSS第１形态\n'),
            TXT(0x0A, '最终BOSS第２形态\n'),
            TXT(0x0B, '最终BOSS第３形态\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_E55'),
        (0x00000001, 'loc_E65'),
        (0x00000002, 'loc_E75'),
        (0x00000003, 'loc_E85'),
        (0x00000004, 'loc_E95'),
        (0x00000005, 'loc_EA5'),
        (0x00000006, 'loc_EB5'),
        (0x00000007, 'loc_EC5'),
        (0x00000008, 'loc_ED5'),
        (0x00000009, 'loc_EE5'),
        (0x0000000A, 'loc_EFB'),
        (0x0000000B, 'loc_F11'),
        (-1, 'loc_F77'),
    )

    def _loc_E55(): pass

    label('loc_E55')

    Battle(0x000007DA, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_F7A')

    def _loc_E65(): pass

    label('loc_E65')

    Battle(0x000007E3, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_F7A')

    def _loc_E75(): pass

    label('loc_E75')

    Battle(0x000007E4, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_F7A')

    def _loc_E85(): pass

    label('loc_E85')

    Battle(0x000007E6, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_F7A')

    def _loc_E95(): pass

    label('loc_E95')

    Battle(0x000007D3, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_F7A')

    def _loc_EA5(): pass

    label('loc_EA5')

    Battle(0x000007D4, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_F7A')

    def _loc_EB5(): pass

    label('loc_EB5')

    Battle(0x000007D5, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_F7A')

    def _loc_EC5(): pass

    label('loc_EC5')

    Battle(0x000007DB, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_F7A')

    def _loc_ED5(): pass

    label('loc_ED5')

    Battle(0x000007DC, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_F7A')

    def _loc_EE5(): pass

    label('loc_EE5')

    PlayBGM(45)
    Call(2, 0x0030)
    Battle(0x000003A1, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_F7A')

    def _loc_EFB(): pass

    label('loc_EFB')

    PlayBGM(46)
    Call(2, 0x0030)
    Battle(0x000003A2, 0x00100008, 0x00, 0x0000, 0xFF)

    Jump('loc_F7A')

    def _loc_F11(): pass

    label('loc_F11')

    PlayBGM(43)
    Call(2, 0x0030)
    SetChrStatus(0x0000, 0xFA, 1)
    SetChrStatus(0x0001, 0xFA, 1)
    SetChrStatus(0x0002, 0xFA, 1)
    SetChrStatus(0x0003, 0xFA, 1)
    SetChrStatus(0x0004, 0xFA, 1)
    SetChrStatus(0x0005, 0xFA, 1)
    SetChrStatus(0x0006, 0xFA, 1)
    SetChrStatus(0x0007, 0xFA, 1)
    SetChrStatus(0x0000, 0x05, 200)
    SetChrStatus(0x0001, 0x05, 200)
    SetChrStatus(0x0002, 0x05, 200)
    SetChrStatus(0x0003, 0x05, 200)
    SetChrStatus(0x0004, 0x05, 200)
    SetChrStatus(0x0005, 0x05, 200)
    SetChrStatus(0x0006, 0x05, 200)
    SetChrStatus(0x0007, 0x05, 200)
    Battle(0x000003B3, 0x0010000A, 0x00, 0x0000, 0xFF)

    Jump('loc_F7A')

    def _loc_F77(): pass

    label('loc_F77')

    Jump('loc_F7A')

    def _loc_F7A(): pass

    label('loc_F7A')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_0D()

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_F91'),
        (-1, 'loc_FBC'),
    )

    def _loc_F91(): pass

    label('loc_F91')

    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)

    Jump('loc_FBC')

    def _loc_FBC(): pass

    label('loc_FBC')

    Jump('func_11_D6F')

    def _loc_FBF(): pass

    label('loc_FBF')

    OP_5F(0x0001)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0012 offset: 0xFCD
@scena.Code('func_12_FCD')
def func_12_FCD():
    ChrTalk(
        0x0000,
        (
            '欢迎',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A9(0x00)

    Return()

# id: 0x0013 offset: 0xFDC
@scena.Code('func_13_FDC')
def func_13_FDC():
    SetChrName('商店君')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪个商店？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        1,
        10,
        100,
        1,
        (
            TXT(0x00, '工房\n'),
            TXT(0x01, '武器店\n'),
            TXT(0x02, '道具店\n'),
            TXT(0x03, '旅馆\n'),
            TXT(0x04, '游击士协会\n'),
            TXT(0x05, '读书（利贝尔通讯１）\n'),
            TXT(0x06, '取消\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_5F(0x0001)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1064'),
        (0x00000001, 'loc_106B'),
        (0x00000002, 'loc_1072'),
        (0x00000003, 'loc_1079'),
        (0x00000004, 'loc_1080'),
        (0x00000005, 'loc_1087'),
        (-1, 'loc_108F'),
    )

    def _loc_1064(): pass

    label('loc_1064')

    Call(0, 0x0012)

    Jump('loc_1092')

    def _loc_106B(): pass

    label('loc_106B')

    Call(0, 0x0014)

    Jump('loc_1092')

    def _loc_1072(): pass

    label('loc_1072')

    Call(0, 0x0015)

    Jump('loc_1092')

    def _loc_1079(): pass

    label('loc_1079')

    Call(0, 0x0016)

    Jump('loc_1092')

    def _loc_1080(): pass

    label('loc_1080')

    Call(0, 0x0017)

    Jump('loc_1092')

    def _loc_1087(): pass

    label('loc_1087')

    OP_B9(0x0347, 0x0000)

    Jump('loc_1092')

    def _loc_108F(): pass

    label('loc_108F')

    Jump('loc_1092')

    def _loc_1092(): pass

    label('loc_1092')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0014 offset: 0x109D
@scena.Code('func_14_109D')
def func_14_109D():
    ChrTalk(
        0x0000,
        (
            '欢迎来到武器店！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A9(0x01)

    Return()

# id: 0x0015 offset: 0x10B8
@scena.Code('func_15_10B8')
def func_15_10B8():
    ChrTalk(
        0x0000,
        (
            '欢迎来到道具店！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A9(0x02)

    Return()

# id: 0x0016 offset: 0x10D3
@scena.Code('func_16_10D3')
def func_16_10D3():
    ChrTalk(
        0x0000,
        (
            '欢迎来到旅馆！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A9(0x03)

    Return()

# id: 0x0017 offset: 0x10EC
@scena.Code('func_17_10EC')
def func_17_10EC():
    ChrTalk(
        0x0000,
        (
            '欢迎来到协会！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_2A(0x0001, 0x0002, 0x0003, 0xFFFF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
