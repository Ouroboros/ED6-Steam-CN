import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0001_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0001   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '居民１'),
    TXT(0x02, '呜喵'),
    TXT(0x03, '宝箱'),
    TXT(0x04, '宝箱'),
    TXT(0x05, ''),
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
    header.entryFunction  = 0x0013
    header.importTable    = ['ED6_DT21/T0001._SN', 'ED6_DT21/T0001_1._SN', 'ED6_DT21/T0001_2._SN', 'ED6_DT21/T0001_3._SN', 'ED6_DT21/T0001_4._SN', 'ED6_DT21/T0001_5._SN', 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1D6F
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
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
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
            talkScenaIndex      = 0x0005,
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

# id: 0x10003 offset: 0x142
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

# id: 0x10004 offset: 0x15E
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

# id: 0x10005 offset: 0x17E
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
            triggerX            = -2000,
            triggerZ            = 1000,
            triggerY            = 0,
            triggerRange        = 2000,
            actorX              = -2000,
            actorZ              = 1000,
            actorY              = 0,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1C6
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x1C7
@scena.Code('Init')
def Init():
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
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 0, 0x1000)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_44F',
    )

    OP_A2(0x1000)
    FormationDelMember(0x00, 0xFF)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF6, 0x00)
    FormationAddMember(ChrTable['克鲁茨'], 0xF7, 0x01)
    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0x02)
    FormationAddMember(ChrTable['尤莉亚上尉'], 0xF9, 0x03)
    Call(2, 0x003A)
    SetChrStatus(ChrTable['艾丝蒂尔'], 0x07, 4)
    SetChrStatus(ChrTable['艾丝蒂尔'], 0x00, 3)
    SetChrStatus(ChrTable['约修亚'], 0x07, 3)
    SetChrStatus(ChrTable['艾丝蒂尔'], 0x07, 3)
    AddCraft(ChrTable['艾丝蒂尔'], CraftTable['助威'])
    AddCraft(ChrTable['艾丝蒂尔'], CraftTable['绞丝棍'])
    AddCraft(ChrTable['艾丝蒂尔'], CraftTable['金刚击'])
    AddCraft(ChrTable['艾丝蒂尔'], CraftTable['旋风轮'])
    AddCraft(ChrTable['艾丝蒂尔'], CraftTable['挑拨'])
    AddCraft(ChrTable['约修亚'], CraftTable['双连击'])
    AddCraft(ChrTable['约修亚'], CraftTable['绝影'])
    AddCraft(ChrTable['约修亚'], CraftTable['挑拨_00A4'])
    AddCraft(ChrTable['约修亚'], CraftTable['胧'])
    AddCraft(ChrTable['约修亚'], CraftTable['魔眼'])
    AddCraft(ChrTable['雪拉扎德'], CraftTable['风之鞭'])
    AddCraft(ChrTable['雪拉扎德'], CraftTable['拘束之鞭'])
    AddCraft(ChrTable['雪拉扎德'], CraftTable['天堂之吻'])
    AddCraft(ChrTable['奥利维尔'], CraftTable['快速狙击'])
    AddCraft(ChrTable['奥利维尔'], CraftTable['精准射击'])
    AddCraft(ChrTable['奥利维尔'], CraftTable['欢乐激发'])
    AddCraft(ChrTable['科洛丝'], CraftTable['斗魂'])
    AddCraft(ChrTable['科洛丝'], CraftTable['岚'])
    AddCraft(ChrTable['阿加特'], CraftTable['公牛之怒'])
    AddCraft(ChrTable['阿加特'], CraftTable['火焰碎击'])
    AddCraft(ChrTable['阿加特'], CraftTable['龙骑之刃'])
    AddCraft(ChrTable['阿加特'], CraftTable['螺旋之刃'])
    AddCraft(ChrTable['提妲'], CraftTable['烟幕弹'])
    AddCraft(ChrTable['提妲'], CraftTable['回复弹'])
    AddCraft(ChrTable['金'], CraftTable['龙神功'])
    AddCraft(ChrTable['金'], CraftTable['养命功'])
    AddCraft(ChrTable['金'], CraftTable['挑拨_00DC'])
    AddCraft(ChrTable['艾丝蒂尔'], CraftTable['连锁战技１(２人协力)'])
    AddCraft(ChrTable['约修亚'], CraftTable['连锁战技１(２人协力)'])
    AddCraft(ChrTable['雪拉扎德'], CraftTable['连锁战技１(２人协力)'])
    AddCraft(ChrTable['奥利维尔'], CraftTable['连锁战技１(２人协力)'])
    AddCraft(ChrTable['科洛丝'], CraftTable['连锁战技１(２人协力)'])
    AddCraft(ChrTable['阿加特'], CraftTable['连锁战技１(２人协力)'])
    AddCraft(ChrTable['提妲'], CraftTable['连锁战技１(２人协力)'])
    AddCraft(ChrTable['金'], CraftTable['连锁战技１(２人协力)'])
    AddSCraft(ChrTable['艾丝蒂尔'], CraftTable['烈波无双击'])
    AddSCraft(ChrTable['艾丝蒂尔'], CraftTable['樱花无双击'])
    AddSCraft(ChrTable['艾丝蒂尔'], CraftTable['奥义·太极轮'])
    AddSCraft(ChrTable['约修亚'], CraftTable['断骨剑'])
    AddSCraft(ChrTable['约修亚'], CraftTable['漆黑之牙'])
    AddSCraft(ChrTable['约修亚'], CraftTable['秘技·幻影奇袭'])
    AddSCraft(ChrTable['雪拉扎德'], CraftTable['女王之怒'])
    AddSCraft(ChrTable['雪拉扎德'], CraftTable['裁决塔罗'])
    AddSCraft(ChrTable['奥利维尔'], CraftTable['咆哮弹'])
    AddSCraft(ChrTable['奥利维尔'], CraftTable['乱心安魂曲'])
    AddSCraft(ChrTable['科洛丝'], CraftTable['光明之环'])
    AddSCraft(ChrTable['科洛丝'], CraftTable['圣星光旋'])
    AddSCraft(ChrTable['阿加特'], CraftTable['霸王疾风'])
    AddSCraft(ChrTable['阿加特'], CraftTable['终极裂斩'])
    AddSCraft(ChrTable['阿加特'], CraftTable['炎龙倒海'])
    AddSCraft(ChrTable['提妲'], CraftTable['炮射冲击'])
    AddSCraft(ChrTable['提妲'], CraftTable['卫星激光'])
    AddSCraft(ChrTable['金'], CraftTable['奥义·龙闪腿'])
    AddSCraft(ChrTable['金'], CraftTable['奥义·雷神掌'])
    AddSCraft(ChrTable['金'], CraftTable['奥义·泰山玄武靠'])
    AddSCraft(ChrTable['乔丝特'], CraftTable['山猫号'])
    AddCraft(ChrTable['凯文神父'], 0x0082)
    AddSCraft(ChrTable['凯文神父'], CraftTable['星杯领域'])
    AddItem(ItemTable['ＨＰ１'], 1)
    AddItem(ItemTable['ＨＰ２'], 1)
    AddItem(ItemTable['攻击１'], 1)
    AddItem(ItemTable['回复药'], 50)
    SetChrStatus(ChrTable['尤莉亚上尉'], 0x00, 85)
    SetChrStatus(ChrTable['尤莉亚上尉'], 0xFE, 0)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['天琴'], 0xFF)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['反射大衣Ⅱ'], 0xFF)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['合成防护靴Ⅱ'], 0xFF)
    AddCraft(ChrTable['尤莉亚上尉'], 0x0000)
    OP_BB(0x0E, 0x06, 0x0000011A)
    OP_37(0x0E, 0x80, 0x03)
    OP_37(0x0E, 0x81, 0x03)
    OP_37(0x0E, 0x82, 0x02)
    OP_37(0x0E, 0x83, 0x03)
    OP_37(0x0E, 0x84, 0x02)
    OP_37(0x0E, 0x85, 0x02)
    OP_37(0x0E, 0x86, 0x02)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['范围'], 0x00)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['行动力３'], 0x01)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['省ＥＰ４'], 0x03)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['ＨＰ４'], 0x04)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['防御４'], 0x05)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['回避４'], 0x06)
    SetChrStatus(ChrTable['穆拉'], 0x00, 86)
    SetChrStatus(ChrTable['穆拉'], 0xFE, 0)
    EquipCmd(ChrTable['穆拉'], ItemTable['耀晶破坏者'], 0xFF)
    EquipCmd(ChrTable['穆拉'], ItemTable['反射大衣Ⅱ'], 0xFF)
    EquipCmd(ChrTable['穆拉'], ItemTable['合成防护靴Ⅱ'], 0xFF)
    AddCraft(ChrTable['穆拉'], 0x0000)
    OP_BB(0x0F, 0x06, 0x00000114)
    OP_37(0x0F, 0x80, 0x02)
    OP_37(0x0F, 0x81, 0x03)
    OP_37(0x0F, 0x82, 0x02)
    OP_37(0x0F, 0x83, 0x02)
    OP_37(0x0F, 0x84, 0x02)
    OP_37(0x0F, 0x85, 0x03)
    OP_37(0x0F, 0x86, 0x03)
    EquipCmd(ChrTable['穆拉'], ItemTable['ＨＰ４'], 0x00)
    EquipCmd(ChrTable['穆拉'], ItemTable['行动力３'], 0x01)
    EquipCmd(ChrTable['穆拉'], ItemTable['攻击４'], 0x02)
    EquipCmd(ChrTable['穆拉'], ItemTable['阴阳'], 0x03)
    EquipCmd(ChrTable['穆拉'], ItemTable['移动３'], 0x04)
    EquipCmd(ChrTable['穆拉'], ItemTable['防御４'], 0x05)
    SetChrStatus(ChrTable['理查德'], 0x00, 85)
    SetChrStatus(ChrTable['理查德'], 0xFE, 0)
    AddCraft(ChrTable['理查德'], 0x0000)
    SetChrStatus(ChrTable['凯诺娜'], 0x00, 85)
    SetChrStatus(ChrTable['凯诺娜'], 0xFE, 0)
    AddCraft(ChrTable['凯诺娜'], 0x0000)
    SetMapFlags(0x01000000)

    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0x00)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0x01)
    FormationAddMember(ChrTable['金'], 0xF8, 0x02)
    FormationAddMember(ChrTable['阿加特'], 0xF9, 0x03)

    AddItem(ItemTable['还魂胶囊'], 99)
    AddItem(ItemTable['还魂粉'], 99)

    OP_BB(0x00, 0x01, 0x00000000)
    OP_BB(0x01, 0x01, 0x00000001)

    for id in range(0x10):
        SetChrStatus(id, 0, 99)     # lv
        SetChrStatus(id, 5, 200)    # cp
        EquipCmd(id, ItemTable['黑耀珠'], 0x00)
        EquipCmd(id, ItemTable['黑耀珠'], 0x01)
        EquipCmd(id, ItemTable['黑耀珠'], 0x02)
        EquipCmd(id, ItemTable['移动３'], 0x03)
        EquipCmd(id, ItemTable['红耀珠'], 0x04)
        EquipCmd(id, ItemTable['红耀珠'], 0x05)
        EquipCmd(id, ItemTable['红耀珠'], 0x06)
        EquipCmd(id, ItemTable['能量宝珠'], 3)
        EquipCmd(id, ItemTable['斗魂腰带'], 4)
        EquipCmd(id, ItemTable['大地女神之服'], 0xFF)
        EquipCmd(id, ItemTable['普罗米修斯神靴'], 0xFF)

    EquipCmd(ChrTable['艾丝蒂尔'], ItemTable['叶隐'], 0x00)

    EquipCmd(ChrTable['艾丝蒂尔'], ItemTable['麒麟具'], 0xFF)
    EquipCmd(ChrTable['约修亚'], ItemTable['凤凰剑（凤·凰）'], 0xFF)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['天狼鞭'], 0xFF)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['殂击神'], 0xFF)
    EquipCmd(ChrTable['科洛丝'], ItemTable['七星剑'], 0xFF)
    EquipCmd(ChrTable['阿加特'], ItemTable['奇剑「鬼灭之刃」'], 0xFF)
    EquipCmd(ChrTable['提妲'], ItemTable['九龙炮'], 0xFF)
    EquipCmd(ChrTable['金'], ItemTable['千手观音'], 0xFF)

    def _loc_44F(): pass

    label('loc_44F')

    SetMapFlags(0x00000001)
    ClearMapFlags(0x00000020)
    ClearMapFlags(0x00400000)

    Return()

# id: 0x0002 offset: 0x45F
@scena.Code('ReInit')
def ReInit():
    OP_D7(0x01, 50000, 0)

    Return()

# id: 0x0003 offset: 0x468
@scena.Code('func_03_468')
def func_03_468():
    Return()

# id: 0x0004 offset: 0x469
@scena.Code('func_04_469')
def func_04_469():
    Call(0, 0x000B)

    Return()

# id: 0x0005 offset: 0x46E
@scena.Code('func_05_46E')
def func_05_46E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_48E',
    )

    ChrTalk(
        0x00FE,
        (
            '立着地点标旗哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_48E(): pass

    label('loc_48E')

    OP_A2(0x0012)
    SetMessageWindowPos(100, 100, 15, 2)

    Talk(
        (
            '#200W可以指定坐标显示哦。',
            TxtCtl.Enter,
            '\n',
            '#W真的哦',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '#20A2等两秒～',
            TxtCtl.Enter,
            '#A如果不指定坐标，\n',
            '画面中央是中心圆（center ring）～',
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
            '#010F#1P停止左上',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#010F#2P停止右上',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#010F#3P停止左下',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#010F#4P停止右下',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#010F#5P停止直上',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#010F#6P停止直下',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要按下F11，就能看见\n',
            '任务区域等地，明白了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#010F我要，和爱娜！白头偕老！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0001,
        (
            '#020F哦哦？哈～哈、哈、哈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0001,
        (
            '#020F没想到会在这种地方\n',
            '遇见爱娜小姐的心上人。',
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
            '#4S啊啊啊啊啊',
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

# id: 0x0006 offset: 0x71B
@scena.Code('func_06_71B')
def func_06_71B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_73F',
    )

    OP_8D(0x00FE, 5000, -5000, 15000, 9000, 2000)
    Yield()

    Jump('func_06_71B')

    def _loc_73F(): pass

    label('loc_73F')

    Return()

# id: 0x0007 offset: 0x740
@scena.Code('func_07_740')
def func_07_740():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_77B',
    )

    OP_70(0x0001, 0x00000032)
    OP_8D(0x00FE, -10000, -10000, 1000, 1000, 2000)
    OP_6F(0x0001, 0)
    OP_72(0x0001, 0x0008)
    Sleep(2000)

    Jump('func_07_740')

    def _loc_77B(): pass

    label('loc_77B')

    Return()

# id: 0x0008 offset: 0x77C
@scena.Code('func_08_77C')
def func_08_77C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_790',
    )

    OP_8C(0x00FE, 180, 5000)
    Yield()

    Jump('func_08_77C')

    def _loc_790(): pass

    label('loc_790')

    Return()

# id: 0x0009 offset: 0x791
@scena.Code('func_09_791')
def func_09_791():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7B4',
    )

    OP_8D(0x0000, 10000, 10000, -10000, -10000, 2000)

    Jump('func_09_791')

    def _loc_7B4(): pass

    label('loc_7B4')

    Return()

# id: 0x000A offset: 0x7B5
@scena.Code('func_0A_7B5')
def func_0A_7B5():
    OP_A1(0x000A, 0x0004)
    SetChrFlags(0x000A, 0x0004)
    ClearChrFlags(0x000A, 0x0100)
    SetChrPos(0x000A, 0, 0, 0, 0)
    OP_98(0x00, 0x000A)
    OP_98(0x01, 0x00002710, 0x000007D0, 0x00002710)
    OP_98(0x01, 0x00001388, 0x00001770, 0x00004E20)

    @scena.Lambda('lambda_07FB')
    def lambda_07FB():
        OP_98(0x02, 0x000A, 0x000007D0, 0x06)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_07FB)

    WaitForThreadExit(0x000A, 0x0002)
    OP_8E(0x000A, -3000, 0, 0, 2000, 0x00)
    OP_98(0x00, 0x000A)
    OP_98(0x01, 0x00001B58, 0x00000000, 0x00001388)
    OP_98(0x01, 0x00002710, 0x000007D0, 0x00001F40)
    OP_98(0x01, 0x00003A98, 0x00001388, 0x00001B58)
    OP_98(0x02, 0x000A, 0x000007D0, 0x02)
    OP_98(0x00, 0x000A)
    OP_98(0x01, 0x00002710, 0xFFFFEC78, 0x000007D0)
    OP_98(0x01, 0x00002710, 0x00002710, 0xFFFFEC78)
    OP_98(0x02, 0x000A, 0x000007D0, 0x02)

    Return()

# id: 0x000B offset: 0x87F
@scena.Code('func_0B_87F')
def func_0B_87F():
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

    Talk(
        (
            '取得号',
            TxtCtl.Enter,
        ),
    )

    OP_57(0x0000, 0x0000, 0x0012, '#1C菜单标题')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_8B2(): pass

    label('loc_8B2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11EB',
    )

    Menu(
        0,
        -1,
        -1,
        1,
        (
            TXT(0x00, '测试地图\n'),
            TXT(0x01, '游戏地图\n'),
            TXT(0x02, '角色一览\n'),
            TXT(0x03, '魔兽一览\n'),
            TXT(0x04, '战斗\n'),
            TXT(0x05, '战斗（魔兽算法测试）\n'),
            TXT(0x06, '战斗（地图确认）\n'),
            TXT(0x07, '迷你游戏\n'),
            TXT(0x08, '事件列表\n'),
            TXT(0x09, '商店测试\n'),
            TXT(0x0A, '前篇后编角色替换新画\n'),
            TXT(0x0B, '*Trap Land\n'),
            TXT(0x0C, '头像\n'),
            TXT(0x0D, '组队选择菜单\n'),
            TXT(0x0E, '*模糊（blur）\n'),
            TXT(0x0F, '道具菜单\n'),
            TXT(0x10, '*出不来！存档菜单\n'),
            TXT(0x11, '手册标志树立完毕\n'),
            TXT(0x12, '菜谱收集完整\n'),
            TXT(0x13, '游戏通关\n'),
            TXT(0x14, 'Camp菜单\n'),
            TXT(0x15, '动画播放·停止\n'),
            TXT(0x16, '队伍变更\n'),
            TXT(0x17, 'Disk Change\n'),
            TXT(0x18, '检查继承标志\n'),
            TXT(0x19, '检查２周目标志（カジノ）\n'),
            TXT(0x1A, '取消\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_16(0x01)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_A82'),
        (0x00000001, 'loc_A89'),
        (0x00000002, 'loc_A90'),
        (0x00000003, 'loc_A97'),
        (0x00000004, 'loc_A9E'),
        (0x00000005, 'loc_AA5'),
        (0x00000006, 'loc_AAC'),
        (0x00000007, 'loc_AB3'),
        (0x00000008, 'loc_ABA'),
        (0x00000009, 'loc_AC4'),
        (0x0000000A, 'loc_AD0'),
        (0x0000000B, 'loc_B7E'),
        (0x0000000C, 'loc_B8A'),
        (0x0000000D, 'loc_D89'),
        (0x0000000E, 'loc_E27'),
        (0x0000000F, 'loc_E62'),
        (0x00000010, 'loc_E69'),
        (0x00000011, 'loc_E6D'),
        (0x00000012, 'loc_E74'),
        (0x00000013, 'loc_E7B'),
        (0x00000014, 'loc_E97'),
        (0x00000015, 'loc_10EA'),
        (0x00000016, 'loc_1117'),
        (0x00000017, 'loc_112B'),
        (0x00000018, 'loc_11CD'),
        (0x00000019, 'loc_11D4'),
        (-1, 'loc_11DB'),
    )

    def _loc_A82(): pass

    label('loc_A82')

    Call(0, 0x000F)

    Jump('loc_11E8')

    def _loc_A89(): pass

    label('loc_A89')

    Call(3, 0x0006)

    Jump('loc_11E8')

    def _loc_A90(): pass

    label('loc_A90')

    Call(3, 0x0000)

    Jump('loc_11E8')

    def _loc_A97(): pass

    label('loc_A97')

    Call(3, 0x0003)

    Jump('loc_11E8')

    def _loc_A9E(): pass

    label('loc_A9E')

    Call(2, 0x0000)

    Jump('loc_11E8')

    def _loc_AA5(): pass

    label('loc_AA5')

    Call(1, 0x0000)

    Jump('loc_11E8')

    def _loc_AAC(): pass

    label('loc_AAC')

    Call(2, 0x0001)

    Jump('loc_11E8')

    def _loc_AB3(): pass

    label('loc_AB3')

    Call(2, 0x003B)

    Jump('loc_11E8')

    def _loc_ABA(): pass

    label('loc_ABA')

    OP_66(0x0001)
    Call(4, 0x0000)

    Jump('loc_11E8')

    def _loc_AC4(): pass

    label('loc_AC4')

    OP_5F(0x0000)
    OP_56(0x00)
    Call(0, 0x0015)

    Jump('loc_11E8')

    def _loc_AD0(): pass

    label('loc_AD0')

    Menu(
        1,
        -1,
        -1,
        1,
        (
            TXT(0x00, '艾丝蒂尔后篇，约修亚后篇\n'),
            TXT(0x01, '艾丝蒂尔前篇，约修亚前篇\n'),
            TXT(0x02, '约修亚后半，科洛丝后半\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_B3A'),
        (0x00000001, 'loc_B4B'),
        (0x00000002, 'loc_B5C'),
        (-1, 'loc_B6D'),
    )

    def _loc_B3A(): pass

    label('loc_B3A')

    OP_BB(0x00, 0x01, 0x00000000)
    OP_BB(0x01, 0x01, 0x00000001)

    Jump('loc_B6D')

    def _loc_B4B(): pass

    label('loc_B4B')

    OP_BB(0x00, 0x01, 0x0000001E)
    OP_BB(0x01, 0x01, 0x0000001F)

    Jump('loc_B6D')

    def _loc_B5C(): pass

    label('loc_B5C')

    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BB(0x01, 0x01, 0x0000001C)

    Jump('loc_B6D')

    def _loc_B6D(): pass

    label('loc_B6D')

    OP_5F(0x0001)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_BD()

    Jump('loc_11E8')

    def _loc_B7E(): pass

    label('loc_B7E')

    NewScene('ED6_DT21/A0019._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_11E8')

    def _loc_B8A(): pass

    label('loc_B8A')

    OP_5F(0x0000)
    OP_56(0x00)
    Sleep(1000)

    OP_D9(0x00, 'CTI00110')
    Sleep(2000)

    OP_D9(0x01)
    OP_C5(0x00, 0x0000, 0x0000, 0x0200, 0x0200, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x01FF, 0x01FF, 0x00FFFFFF, 0x00, 'C_VIS000._CH')
    OP_C6(0x00, 0x03, -1, 1000, 0)
    Sleep(2000)

    OP_C5(0x01, 0xFF9C, 0xFF9C, 0x0064, 0x0064, 0x0154, 0x00FA, 0x0300, 0x0200, 0x0000, 0x0000, 0x00FF, 0x00FF, 0x00FFFFFF, 0x00, 'C_VIS001._CH')
    OP_C6(0x01, 0x03, -1, 1000, 0)
    Sleep(2000)

    OP_C5(0x00, 0xFF9C, 0xFF9C, 0x0064, 0x0064, 0x0168, 0x0104, 0x0300, 0x0200, 0x0000, 0x0000, 0x00FF, 0x00FF, 0x00FFFFFF, 0x00, 'C_VIS002._CH')
    OP_C6(0x00, 0x03, -1, 1000, 0)
    Sleep(2000)

    OP_C5(0x02, 0xFF9C, 0xFF9C, 0x0064, 0x0064, 0x017C, 0x0104, 0x0300, 0x0200, 0x0000, 0x0000, 0x00FF, 0x00FF, 0x00FFFFFF, 0x00, 'C_VIS002._CH')
    OP_C6(0x02, 0x03, -1, 1000, 0)
    Sleep(2000)

    OP_C5(0x03, 0xFF9C, 0xFF9C, 0x0064, 0x0064, 0x0190, 0x0104, 0x0300, 0x0200, 0x0000, 0x0000, 0x00FF, 0x00FF, 0x00FFFFFF, 0x00, 'C_VIS002._CH')
    OP_C6(0x03, 0x03, -1, 1000, 0)
    OP_C6(0x00, 0x00, 0, 0, 1000)
    OP_C6(0x00, 0x02, 90000, 2000, 0)
    OP_C7(0x00, 0x00, 0x00)

    Talk(
        (
            '噢',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x00, 0x00, 360000, 260000, 0)
    Sleep(1000)

    OP_C6(0x01, 0x04, 0, 0, 0)
    Sleep(1000)

    OP_C6(0x00, 0x03, 16777215, 1000, 0)
    OP_C6(0x00, 0x01, 0, 1000, 1000)
    OP_C6(0x01, 0x03, 16777215, 1000, 0)
    OP_C6(0x02, 0x03, 16777215, 500, 0)
    OP_C6(0x03, 0x01, 10000, 0, 500)
    OP_C7(0x00, 0xFF, 0x03)
    OP_C7(0x01, 0xFF, 0x00)

    Jump('loc_11E8')

    def _loc_D89(): pass

    label('loc_D89')

    OP_5F(0x0000)
    OP_56(0x00)

    OP_C9(
        0x00,
        (
            0x0000,
            0x00FF,
            0x00FF,
            0x00FF,
        ),
        (
            0x0001,
            0x0002,
            0x0003,
            0x0004,
            0x0005,
            0x0006,
            0x0007,
            0x0008,
            0x0009,
            0x000D,
            0x000A,
            0x000F,
            0x000E,
            0x000B,
            0x000C,
            0xFFFF,
        ),
    )

    ChrTalk(
        0x00F8,
        (
            'Ｏｋ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DE4',
    )

    ChrTalk(
        0x00F7,
        (
            '队友１科洛丝',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_E23')

    def _loc_DE4(): pass

    label('loc_DE4')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E05',
    )

    ChrTalk(
        0x00F7,
        (
            '队友１约修亚',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_E23')

    def _loc_E05(): pass

    label('loc_E05')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E23',
    )

    ChrTalk(
        0x00F7,
        (
            '队友１阿加特',
            TxtCtl.Enter,
        ),
    )

    def _loc_E23(): pass

    label('loc_E23')

    CloseMessageWindow()

    Jump('loc_11E8')

    def _loc_E27(): pass

    label('loc_E27')

    OP_14(0x000003E8, 0xBBFFFFFF, 0x00000000, 0x00, 0x00000000)

    ChrTalk(
        0x00F6,
        (
            '*模糊（blur）',
            TxtCtl.Enter,
        ),
    )

    Sleep(2000)

    OP_15(0x000001F4)

    ChrTalk(
        0x00F6,
        (
            '那么',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11E8')

    def _loc_E62(): pass

    label('loc_E62')

    OP_18(0x00, 0x00, 0x00)

    Jump('loc_11E8')

    def _loc_E69(): pass

    label('loc_E69')

    ShowSaveMenu()

    Jump('loc_11E8')

    def _loc_E6D(): pass

    label('loc_E6D')

    Call(5, 0x0000)

    Jump('loc_11E8')

    def _loc_E74(): pass

    label('loc_E74')

    Call(5, 0x0001)

    Jump('loc_11E8')

    def _loc_E7B(): pass

    label('loc_E7B')

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0x12B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x22AE)
    FadeOut(500, 0, -1)
    ShowSaveMenu()
    OP_B4(0x01)

    Jump('loc_11E8')

    def _loc_E97(): pass

    label('loc_E97')

    EventBegin(0x00)
    OP_5F(0x0000)
    OP_56(0x00)
    OP_A3(0x0016)
    def _loc_EA1(): pass

    label('loc_EA1')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_10D4',
    )

    FadeOut(1000, 0, -1)
    OP_0D()

    Talk(
        (
            TxtCtl.ShowAll,
            0x18,
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　更换队员，进行必要的装备变更，\n',
            '　确定后，请选择【继续】。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【编成队伍】\n'),
            TXT(0x01, '【变更装备】\n'),
            TXT(0x02, '【继续】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FCC',
    )

    OP_A2(0x0016)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　请选择２名固定成员以外的同行者。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(100)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0008,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0003,
            0x0004,
            0x0007,
            0xFFFF,
        ),
    )

    Jump('loc_10D1')

    def _loc_FCC(): pass

    label('loc_FCC')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1037',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 6, 0x16)),
            Expr.Return,
        ),
        'loc_1005',
    )

    OP_C0(0x13, 0x00000078, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    Jump('loc_1034')

    def _loc_1005(): pass

    label('loc_1005')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※请在进行队伍的编组之后再选择。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(100)

    def _loc_1034(): pass

    label('loc_1034')

    Jump('loc_10D1')

    def _loc_1037(): pass

    label('loc_1037')

    SetChrName('')

    Talk(
        (
            TxtCtl.ShowAll,
            0x18,
            (TxtCtl.SetColor, 0x5),
            '可以继续事件剧情了吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10B5',
    )

    SetChrName('')

    Talk(
        (
            TxtCtl.ShowAll,
            0x18,
            (TxtCtl.SetColor, 0x5),
            '继续事件发展。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_10D4')

    def _loc_10B5(): pass

    label('loc_10B5')

    SetChrName('')

    Talk(
        (
            TxtCtl.ShowAll,
            0x18,
            (TxtCtl.SetColor, 0x5),
            '返回选择画面。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_10D1(): pass

    label('loc_10D1')

    Jump('loc_EA1')

    def _loc_10D4(): pass

    label('loc_10D4')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeIn(0, 0)
    OP_0D()

    Jump('loc_11E8')

    def _loc_10EA(): pass

    label('loc_10EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Return,
        ),
        'loc_10FE',
    )

    PlayMovie(0x01, '', 0x0000, 0x0000)
    OP_A3(0x0015)

    Jump('loc_1114')

    def _loc_10FE(): pass

    label('loc_10FE')

    PlayMovie(0x00, 'ED6_DT41.dat', 0x0000, 0x0000)
    OP_A2(0x0015)

    def _loc_1114(): pass

    label('loc_1114')

    Jump('loc_11E8')

    def _loc_1117(): pass

    label('loc_1117')

    Call(0, 0x001B)
    FadeIn(0, 0)
    Call(0, 0x001C)

    Jump('loc_11E8')

    def _loc_112B(): pass

    label('loc_112B')

    OP_5F(0x0000)

    Talk(
        (
            'RAM Saving!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_E9(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xCA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_115D',
    )

    Talk(
        (
            'RAM Load！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_115D(): pass

    label('loc_115D')

    Talk(
        (
            'Disk chaaaaange!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0xC8),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1184',
    )

    OP_E6(0x02)

    Jump('loc_1186')

    def _loc_1184(): pass

    label('loc_1184')

    OP_E6(0x01)

    def _loc_1186(): pass

    label('loc_1186')

    If(
        (
            (Expr.PushValueByIndex, 0xC9),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11AD',
    )

    Talk(
        (
            'RAM Load\n',
            'completed!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_E9(0x02)

    def _loc_11AD(): pass

    label('loc_11AD')

    Talk(
        (
            'RAM Delete\n',
            'completed!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_E9(0x00)

    Jump('loc_11E8')

    def _loc_11CD(): pass

    label('loc_11CD')

    Call(0, 0x000C)

    Jump('loc_11E8')

    def _loc_11D4(): pass

    label('loc_11D4')

    Call(0, 0x000D)

    Jump('loc_11E8')

    def _loc_11DB(): pass

    label('loc_11DB')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_11E8')

    def _loc_11E8(): pass

    label('loc_11E8')

    Jump('loc_8B2')

    def _loc_11EB(): pass

    label('loc_11EB')

    OP_5F(0x0000)
    OP_56(0x00)
    OP_DA()
    Sleep(300)

    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x11F9
@scena.Code('func_0C_11F9')
def func_0C_11F9():
    EventBegin(0x00)
    OP_5F(0x0000)
    OP_5F(0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 2, 0x1042)),
            Expr.Return,
        ),
        'loc_1231',
    )

    Talk(
        (
            'Equipment\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_1252')

    def _loc_1231(): pass

    label('loc_1231')

    Talk(
        (
            'Equipment\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_1252(): pass

    label('loc_1252')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 3, 0x1043)),
            Expr.Return,
        ),
        'loc_127F',
    )

    Talk(
        (
            'Items\n',
            'have been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_129C')

    def _loc_127F(): pass

    label('loc_127F')

    Talk(
        (
            'Items\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_129C(): pass

    label('loc_129C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 5, 0x1045)),
            Expr.Return,
        ),
        'loc_12C9',
    )

    Talk(
        (
            'Status\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_12E7')

    def _loc_12C9(): pass

    label('loc_12C9')

    Talk(
        (
            'Status\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_12E7(): pass

    label('loc_12E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 6, 0x1046)),
            Expr.Return,
        ),
        'loc_1312',
    )

    Talk(
        (
            'Mira\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_132E')

    def _loc_1312(): pass

    label('loc_1312')

    Talk(
        (
            'Mira\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_132E(): pass

    label('loc_132E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 4, 0x1044)),
            Expr.Return,
        ),
        'loc_135D',
    )

    Talk(
        (
            'Notebook\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_137D')

    def _loc_135D(): pass

    label('loc_135D')

    Talk(
        (
            'Notebook\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_137D(): pass

    label('loc_137D')

    If(
        (
            (Expr.Eval, "OP_40(0x0208, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.Eval, "OP_40(0x035C, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_13C5',
    )

    Talk(
        (
            'FC Clear Data\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_13EA')

    def _loc_13C5(): pass

    label('loc_13C5')

    Talk(
        (
            'FC Clear Data\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_13EA(): pass

    label('loc_13EA')

    Return()

# id: 0x000D offset: 0x13EB
@scena.Code('func_0D_13EB')
def func_0D_13EB():
    EventBegin(0x00)
    OP_5F(0x0000)
    OP_5F(0x0001)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14D4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0455, 6, 0x22AE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_146B',
    )

    Talk(
        (
            'SC Clear Data\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            'Since it\x27s Chapter 8,\n',
            'opening Chapter 8 Casino Shop.',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A9(0x6C)

    Jump('loc_14D1')

    def _loc_146B(): pass

    label('loc_146B')

    Talk(
        (
            'SC Clear Data\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            'Since it\x27s Chapter 8,\n',
            'opening Chapter 8 Casino Shop.',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A9(0x80)

    def _loc_14D1(): pass

    label('loc_14D1')

    Jump('loc_15AE')

    def _loc_14D4(): pass

    label('loc_14D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0455, 6, 0x22AE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1544',
    )

    Talk(
        (
            'SC Clear Data\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            'Since it\x27s not Chapter 8,\n',
            'opening Chapter 1 Casino Shop.',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A9(0x69)

    Jump('loc_15AE')

    def _loc_1544(): pass

    label('loc_1544')

    Talk(
        (
            'SC Clear Data\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            'Since it\x27s not Chapter 8,\n',
            'opening Chapter 1 Casino Shop.',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A9(0x7D)

    def _loc_15AE(): pass

    label('loc_15AE')

    Return()

# id: 0x000E offset: 0x15AF
@scena.Code('func_0E_15AF')
def func_0E_15AF():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1870',
    )

    Menu(
        1,
        10,
        100,
        1,
        (
            TXT(0x00, 'Equipment\n'),
            TXT(0x01, 'Items\n'),
            TXT(0x02, 'Status\n'),
            TXT(0x03, 'Mira\n'),
            TXT(0x04, 'Notebook\n'),
            TXT(0x05, 'FC Clear Data\n'),
            TXT(0x06, 'Cancel\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_5F(0x0001)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1629'),
        (0x00000001, 'loc_1687'),
        (0x00000002, 'loc_16DE'),
        (0x00000003, 'loc_1736'),
        (0x00000004, 'loc_178A'),
        (0x00000005, 'loc_17E6'),
        (-1, 'loc_1860'),
    )

    def _loc_1629(): pass

    label('loc_1629')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 2, 0x1042)),
            Expr.Return,
        ),
        'loc_1659',
    )

    Talk(
        (
            'Equipment\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_167A')

    def _loc_1659(): pass

    label('loc_1659')

    Talk(
        (
            'Equipment\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_167A(): pass

    label('loc_167A')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_186D')

    def _loc_1687(): pass

    label('loc_1687')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 3, 0x1043)),
            Expr.Return,
        ),
        'loc_16B4',
    )

    Talk(
        (
            'Items\n',
            'have been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_16D1')

    def _loc_16B4(): pass

    label('loc_16B4')

    Talk(
        (
            'Items\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_16D1(): pass

    label('loc_16D1')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_186D')

    def _loc_16DE(): pass

    label('loc_16DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 5, 0x1045)),
            Expr.Return,
        ),
        'loc_170B',
    )

    Talk(
        (
            'Status\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_1729')

    def _loc_170B(): pass

    label('loc_170B')

    Talk(
        (
            'Status\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_1729(): pass

    label('loc_1729')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_186D')

    def _loc_1736(): pass

    label('loc_1736')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 6, 0x1046)),
            Expr.Return,
        ),
        'loc_1761',
    )

    Talk(
        (
            'Mira\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_177D')

    def _loc_1761(): pass

    label('loc_1761')

    Talk(
        (
            'Mira\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_177D(): pass

    label('loc_177D')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_186D')

    def _loc_178A(): pass

    label('loc_178A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 4, 0x1044)),
            Expr.Return,
        ),
        'loc_17B9',
    )

    Talk(
        (
            'Notebook\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_17D9')

    def _loc_17B9(): pass

    label('loc_17B9')

    Talk(
        (
            'Notebook\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_17D9(): pass

    label('loc_17D9')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_186D')

    def _loc_17E6(): pass

    label('loc_17E6')

    If(
        (
            (Expr.Eval, "OP_40(0x0208, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.Eval, "OP_40(0x035C, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_182E',
    )

    Talk(
        (
            'FC Clear Data\n',
            'has been carried over!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_1853')

    def _loc_182E(): pass

    label('loc_182E')

    Talk(
        (
            'FC Clear Data\n',
            'not carried over?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_1853(): pass

    label('loc_1853')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_186D')

    def _loc_1860(): pass

    label('loc_1860')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_186D')

    def _loc_186D(): pass

    label('loc_186D')

    Jump('func_0E_15AF')

    def _loc_1870(): pass

    label('loc_1870')

    Return()

# id: 0x000F offset: 0x1871
@scena.Code('func_0F_1871')
def func_0F_1871():
    Talk(
        (
            TxtCtl.ShowAll,
            '请选择测试地图哦。',
            TxtCtl.Enter,
        ),
    )

    def _loc_1887(): pass

    label('loc_1887')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19AB',
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
            TXT(0x08, '测试地图28\n'),
            TXT(0x09, '测试地图29\n'),
            TXT(0x0A, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1944'),
        (0x00000001, 'loc_194D'),
        (0x00000002, 'loc_1956'),
        (0x00000003, 'loc_195F'),
        (0x00000004, 'loc_1968'),
        (0x00000005, 'loc_1971'),
        (0x00000006, 'loc_197A'),
        (0x00000007, 'loc_1983'),
        (0x00000008, 'loc_198C'),
        (0x00000009, 'loc_1995'),
        (-1, 'loc_199E'),
    )

    def _loc_1944(): pass

    label('loc_1944')

    NewScene('ED6_DT21/T0020._SN', 0, 0, 0)
    IdleLoop()

    def _loc_194D(): pass

    label('loc_194D')

    NewScene('ED6_DT21/T0021._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1956(): pass

    label('loc_1956')

    NewScene('ED6_DT21/T0022._SN', 0, 0, 0)
    IdleLoop()

    def _loc_195F(): pass

    label('loc_195F')

    NewScene('ED6_DT21/T0023._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1968(): pass

    label('loc_1968')

    NewScene('ED6_DT21/T0024._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1971(): pass

    label('loc_1971')

    NewScene('ED6_DT21/T0025._SN', 0, 0, 0)
    IdleLoop()

    def _loc_197A(): pass

    label('loc_197A')

    NewScene('ED6_DT21/T0026._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1983(): pass

    label('loc_1983')

    NewScene('ED6_DT21/T0027._SN', 0, 0, 0)
    IdleLoop()

    def _loc_198C(): pass

    label('loc_198C')

    NewScene('ED6_DT21/T0028._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1995(): pass

    label('loc_1995')

    NewScene('ED6_DT21/T0029._SN', 0, 0, 0)
    IdleLoop()

    def _loc_199E(): pass

    label('loc_199E')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1887')

    def _loc_19AB(): pass

    label('loc_19AB')

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

# id: 0x0010 offset: 0x19BB
@scena.Code('func_10_19BB')
def func_10_19BB():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪个？',
            TxtCtl.Enter,
        ),
    )

    def _loc_19C5(): pass

    label('loc_19C5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A27',
    )

    Menu(
        1,
        10,
        100,
        1,
        (
            TXT(0x00, '地图目标1\n'),
            TXT(0x01, '地图目标2\n'),
            TXT(0x02, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1A08'),
        (0x00000001, 'loc_1A11'),
        (-1, 'loc_1A1A'),
    )

    def _loc_1A08(): pass

    label('loc_1A08')

    NewScene('ED6_DT21/T0070._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1A11(): pass

    label('loc_1A11')

    NewScene('ED6_DT21/T0071._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1A1A(): pass

    label('loc_1A1A')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_19C5')

    def _loc_1A27(): pass

    label('loc_1A27')

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

# id: 0x0011 offset: 0x1A37
@scena.Code('func_11_1A37')
def func_11_1A37():
    OP_6B(5000, 3000)
    Call(0, 0x0012)

    Return()

# id: 0x0012 offset: 0x1A45
@scena.Code('func_12_1A45')
def func_12_1A45():
    OP_6C(0, 20000)

    Return()

# id: 0x0013 offset: 0x1A4F
@scena.Code('func_13_1A4F')
def func_13_1A4F():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x382),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A98',
    )

    EventBegin(0x00)
    OP_C2()

    If(
        (
            (Expr.Eval, "OP_CD(0x0009)"),
            Expr.Return,
        ),
        'loc_1A85',
    )

    Sleep(1000)

    OP_62(0x0000, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)

    Jump('loc_1A93')

    def _loc_1A85(): pass

    label('loc_1A85')

    Talk(
        (
            '没有反应',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_1A93(): pass

    label('loc_1A93')

    EventEnd(0x00)

    Jump('loc_1AB6')

    def _loc_1A98(): pass

    label('loc_1A98')

    Talk(
        (
            '什么也没有发生(ByScript)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    def _loc_1AB6(): pass

    label('loc_1AB6')

    Return()

# id: 0x0014 offset: 0x1AB7
@scena.Code('func_14_1AB7')
def func_14_1AB7():
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

# id: 0x0015 offset: 0x1AC6
@scena.Code('func_15_1AC6')
def func_15_1AC6():
    SetChrName('Sara')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪个店？',
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
            TXT(0x03, '旅店\n'),
            TXT(0x04, '协会\n'),
            TXT(0x05, '读书（利贝尔通讯１）\n'),
            TXT(0x06, '娱乐场交换处\n'),
            TXT(0x07, '取消\n'),
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
        (0x00000000, 'loc_1B55'),
        (0x00000001, 'loc_1B5C'),
        (0x00000002, 'loc_1B63'),
        (0x00000003, 'loc_1B6A'),
        (0x00000004, 'loc_1B71'),
        (0x00000005, 'loc_1B78'),
        (0x00000006, 'loc_1B80'),
        (-1, 'loc_1B87'),
    )

    def _loc_1B55(): pass

    label('loc_1B55')

    Call(0, 0x0014)

    Jump('loc_1B8A')

    def _loc_1B5C(): pass

    label('loc_1B5C')

    Call(0, 0x0016)

    Jump('loc_1B8A')

    def _loc_1B63(): pass

    label('loc_1B63')

    Call(0, 0x0017)

    Jump('loc_1B8A')

    def _loc_1B6A(): pass

    label('loc_1B6A')

    Call(0, 0x0018)

    Jump('loc_1B8A')

    def _loc_1B71(): pass

    label('loc_1B71')

    Call(0, 0x0019)

    Jump('loc_1B8A')

    def _loc_1B78(): pass

    label('loc_1B78')

    OP_B8(0x0347, 0x0000)

    Jump('loc_1B8A')

    def _loc_1B80(): pass

    label('loc_1B80')

    Call(0, 0x001A)

    Jump('loc_1B8A')

    def _loc_1B87(): pass

    label('loc_1B87')

    Jump('loc_1B8A')

    def _loc_1B8A(): pass

    label('loc_1B8A')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0016 offset: 0x1B95
@scena.Code('func_16_1B95')
def func_16_1B95():
    ChrTalk(
        0x0000,
        (
            '欢迎光临武器店！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A9(0x01)

    Return()

# id: 0x0017 offset: 0x1BB0
@scena.Code('func_17_1BB0')
def func_17_1BB0():
    ChrTalk(
        0x0000,
        (
            '欢迎光临道具店！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A9(0x02)

    Return()

# id: 0x0018 offset: 0x1BCB
@scena.Code('func_18_1BCB')
def func_18_1BCB():
    ChrTalk(
        0x0000,
        (
            '欢迎光临旅店！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A9(0x05)

    Return()

# id: 0x0019 offset: 0x1BE4
@scena.Code('func_19_1BE4')
def func_19_1BE4():
    ChrTalk(
        0x0000,
        (
            '欢迎光临游击士协会！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_2A(0x0065, 0x0066, 0x0001, 0xFFFF)

    Return()

# id: 0x001A offset: 0x1C0A
@scena.Code('func_1A_1C0A')
def func_1A_1C0A():
    ChrTalk(
        0x0000,
        (
            '这里是交换所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A9(0x69)

    Return()

# id: 0x001B offset: 0x1C23
@scena.Code('func_1B_1C23')
def func_1B_1C23():
    FadeOut(0, 0, -1)
    FormationReset()
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, 'Set Scherazard as Partner\n'),
            TXT(0x01, 'Set Agate as Partner\n'),
        ),
    )

    MenuEnd(0x0000)

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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1CA0'),
        (0x00000001, 'loc_1CA6'),
        (-1, 'loc_1CAC'),
    )

    def _loc_1CA0(): pass

    label('loc_1CA0')

    OP_A2(0x1200)

    Jump('loc_1CAC')

    def _loc_1CA6(): pass

    label('loc_1CA6')

    OP_A2(0x1201)

    Jump('loc_1CAC')

    def _loc_1CAC(): pass

    label('loc_1CAC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1CCA',
    )

    Talk(
        (
            'ほげっちゃ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_1CCE')

    def _loc_1CCA(): pass

    label('loc_1CCA')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_1CCE(): pass

    label('loc_1CCE')

    Return()

# id: 0x001C offset: 0x1CCF
@scena.Code('func_1C_1CCF')
def func_1C_1CCF():
    ClearMapFlags(0x00000001)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            0x0000,
            0x00FF,
            0x00FF,
            0x00FF,
        ),
        (
            0x0001,
            0x0002,
            0x0003,
            0x0004,
            0x0005,
            0x0006,
            0x0007,
            0x0008,
            0x0009,
            0x000D,
            0x000A,
            0x000F,
            0x000E,
            0x000B,
            0x000C,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)
    Sleep(1000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
