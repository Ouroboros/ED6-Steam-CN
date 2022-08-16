import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0133_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0133   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0133.x'
    header.mapIndex       = 10
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00001770,
            dword_04        = 0x00000000,
            dword_08        = 0x0002CEC0,
            word_0C         = 0x0004,
            word_0E         = 0x010E,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 10,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
    ]

# id: 0x10001 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '潘杜爷爷',
            x                   = 3275,
            z                   = 0,
            y                   = 2522,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '艾娅莉',
            x                   = 54174,
            z                   = 10300,
            y                   = 44126,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '阿鲁姆',
            x                   = 54904,
            z                   = 10300,
            y                   = 44125,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
    )

# id: 0x10002 offset: 0x122
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x122
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x122
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -300,
            triggerZ            = 0,
            triggerY            = 4140,
            triggerRange        = 800,
            actorX              = -300,
            actorZ              = 1000,
            actorY              = 4140,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 53450,
            triggerZ            = 10300,
            triggerY            = 47970,
            triggerRange        = 800,
            actorX              = 53450,
            actorZ              = 10000,
            actorY              = 47970,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x16A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_17E',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0008)

    Jump('loc_1D3')

    def _loc_17E(): pass

    label('loc_17E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_188',
    )

    Jump('loc_1D3')

    def _loc_188(): pass

    label('loc_188')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_19C',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0008)

    Jump('loc_1D3')

    def _loc_19C(): pass

    label('loc_19C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_1A6',
    )

    Jump('loc_1D3')

    def _loc_1A6(): pass

    label('loc_1A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_1C4',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0008)

    Jump('loc_1D3')

    def _loc_1C4(): pass

    label('loc_1C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_1CE',
    )

    Jump('loc_1D3')

    def _loc_1CE(): pass

    label('loc_1CE')

    ChrSetFlags(0x0008, 0x0010)

    def _loc_1D3(): pass

    label('loc_1D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_1E1',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_09_D4C)

    def _loc_1E1(): pass

    label('loc_1E1')

    Return()

# id: 0x0001 offset: 0x1E2
@scena.Code('func_01_1E2')
def func_01_1E2():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1FA',
    )

    OP_B1('t0133_y')

    Jump('loc_203')

    def _loc_1FA(): pass

    label('loc_1FA')

    OP_B1('t0133_n')

    def _loc_203(): pass

    label('loc_203')

    Return()

# id: 0x0002 offset: 0x204
@scena.Code('func_02_204')
def func_02_204():
    Return()

# id: 0x0003 offset: 0x205
@scena.Code('func_03_205')
def func_03_205():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_21A',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_03_205')

    def _loc_21A(): pass

    label('loc_21A')

    Return()

# id: 0x0004 offset: 0x21B
@scena.Code('func_04_21B')
def func_04_21B():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_341',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2EE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '每天从塔顶向外眺望，\n',
            '真是让人很开心呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '季节的变化，\n',
            '城镇里人们的生活……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每天都会发生\n',
            '各种各样的变化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近经常在街上看到\n',
            '布露姆老太太。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '她要去干什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33E')

    def _loc_2EE(): pass

    label('loc_2EE')

    ChrTalk(
        0x00FE,
        (
            '每天从塔顶向外眺望，\n',
            '真是让人很开心呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每天都会发生\n',
            '各种各样的变化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_33E(): pass

    label('loc_33E')

    Jump('loc_8A3')

    def _loc_341(): pass

    label('loc_341')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_441',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '战争结束，修复钟楼的时候，\n',
            '梅尔达斯的儿子\n',
            '把大钟改成了导力驱动式。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我能摆弄的部分越来越少了，\n',
            '真是感到有些寂寞啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '这也是时代的变迁呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_43E')

    def _loc_3F6(): pass

    label('loc_3F6')

    ChrTalk(
        0x00FE,
        (
            '战争结束，修复钟楼的时候，\n',
            '梅尔达斯的儿子\n',
            '把大钟改成了导力驱动式。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_43E(): pass

    label('loc_43E')

    Jump('loc_8A3')

    def _loc_441(): pass

    label('loc_441')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_504',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4BB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '开始今天的检查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个塔是洛连特的象征，\n',
            '代表了洛连特的历史，\n',
            '而且也是我的骄傲呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_501')

    def _loc_4BB(): pass

    label('loc_4BB')

    ChrTalk(
        0x00FE,
        (
            '这个塔是洛连特的象征，\n',
            '代表了洛连特的历史，\n',
            '而且也是我的骄傲呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_501(): pass

    label('loc_501')

    Jump('loc_8A3')

    def _loc_504(): pass

    label('loc_504')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_5EC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_59B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '一天又过去了， \n',
            '和平的日子实在是比什么都好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '一想起十年前的那次战争我就忍不住颤抖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '战争什么的……不要再发生了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5E9')

    def _loc_59B(): pass

    label('loc_59B')

    ChrTalk(
        0x0008,
        (
            '一想起十年前的那次战争我就忍不住颤抖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '战争什么的……不要再发生了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5E9(): pass

    label('loc_5E9')

    Jump('loc_8A3')

    def _loc_5EC(): pass

    label('loc_5EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_6DA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_691',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '还是老样子，\n',
            '钟声依旧那么动听。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我呀，\n',
            '最喜欢听这个塔的钟声呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这个钟不仅仅\n',
            '只有报时的作用哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '它还铭刻着\n',
            '洛连特的历史呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6D7')

    def _loc_691(): pass

    label('loc_691')

    ChrTalk(
        0x0008,
        (
            '这个钟不仅仅\n',
            '只有报时的作用哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '它还铭刻着\n',
            '洛连特的历史呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6D7(): pass

    label('loc_6D7')

    Jump('loc_8A3')

    def _loc_6DA(): pass

    label('loc_6DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_858',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0101,
        (
            '#001F潘杜爷爷！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '嗯？这个声音是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '……呵呵呵呵！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我还以为是谁呢，\n',
            '这不是卡西乌斯家的\n',
            '调皮姑娘和听话小子吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '最近你们好久都\n',
            '没有到这里来玩了呢，\n',
            '这段时间很忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F潘杜爷爷还是一直都在这里守着的吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '这里就像\n',
            '我的家一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我会一直守着这个钟楼，\n',
            '至死方休。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8A3')

    def _loc_858(): pass

    label('loc_858')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x0008,
        (
            '这里就像\n',
            '我的家一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我会一直守着这个钟楼，\n',
            '至死方休。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8A3(): pass

    label('loc_8A3')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x8A7
@scena.Code('func_05_8A7')
def func_05_8A7():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9E9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '星星开始闪烁的时候，\n',
            '他在塔上这么和我说的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '可以和我交往吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '哎呀㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这就是我\n',
            '梦寐以求的场景啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 180, 500)

    ChrTalk(
        0x0101,
        (
            '#501F（唔，\n',
            '　的确是一个相当不错的地方……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#501F（为了听这句话\n',
            '　两个人特意跑上这里来？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（呵呵……\n',
            '　这要看当事人是怎么想的了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A29')

    def _loc_9E9(): pass

    label('loc_9E9')

    ChrTalk(
        0x0009,
        (
            '呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好·幸·福·呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    def _loc_A29(): pass

    label('loc_A29')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0xA2D
@scena.Code('func_06_A2D')
def func_06_A2D():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B3D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000A,
        (
            '#4S成功了！#3S',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '听我说！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '她终于答应\n',
            '和我交往了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 180, 500)
    OP_62(0x000A, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '啊啊，女神大人……\n',
            '一整天所做的努力终于没有白费啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#501F（一、一整天……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（真是坚持不懈换来的胜利呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B76')

    def _loc_B3D(): pass

    label('loc_B3D')

    ChrTalk(
        0x000A,
        (
            '啊啊，女神大人……\n',
            '一整天所做的努力终于没有白费啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B76(): pass

    label('loc_B76')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0xB7A
@scena.Code('func_07_B7A')
def func_07_B7A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 2, 0x26A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0072, 0, 0x390)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D38',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x004D, 2, 0x26A))
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这里有架梯子可以通到上面的瞭望台去。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010020136V#003F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020020137V#014F哟，怎么了？\n',
            '突然愣着不动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010020138V#506F啊……唔唔，没什么！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020139V#006F对了，我们也上瞭望台看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020140V#014F唔……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D27',
    )

    ChrTalk(
        0x0103,
        (
            '#0030020141V#522F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D27(): pass

    label('loc_D27')

    Sleep(100)

    NewScene('ED6_DT01/T0133._SN', 103, 0, 0)
    IdleLoop()

    Jump('loc_D41')

    def _loc_D38(): pass

    label('loc_D38')

    NewScene('ED6_DT01/T0133._SN', 103, 0, 0)
    IdleLoop()
    def _loc_D41(): pass

    label('loc_D41')

    Return()

# id: 0x0008 offset: 0xD42
@scena.Code('func_08_D42')
def func_08_D42():
    NewScene('ED6_DT01/T0133._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0xD4C
@scena.Code('func_09_D4C')
def func_09_D4C():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    ChrSetPos(0x0101, 54192, 10300, 44126, 180)
    ChrSetPos(0x0102, 55561, 10300, 44126, 180)
    MapSetFlags(0x00000010)
    FadeIn(4000, 0)
    CameraMove(54670, 10300, 44190, 0)
    OP_6C(330000, 0)
    OP_67(0, 8300, -10000, 0)
    CameraSetDistance(1560, 0)
    OP_6E(457, 0)

    @scena.Lambda('lambda_0DC6')
    def lambda_0DC6():
        CameraMove(54190, 10300, 41950, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0DC6)

    @scena.Lambda('lambda_0DDE')
    def lambda_0DDE():
        OP_6C(302000, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0DDE)

    @scena.Lambda('lambda_0DEE')
    def lambda_0DEE():
        OP_6E(539, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_0DEE)

    @scena.Lambda('lambda_0DFE')
    def lambda_0DFE():
        OP_67(0, 7060, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0DFE)

    Sleep(6500)

    Fade(1500)
    CameraMove(54620, 10300, 44190, 0)
    OP_67(0, 6690, -10000, 0)
    CameraSetDistance(1660, 0)
    OP_6C(225000, 0)
    OP_6E(476, 0)
    ChrSetPos(0x0101, 53950, 10300, 44150, 180)
    ChrSetPos(0x0102, 55250, 10300, 44150, 180)
    Sleep(2000)

    ChrTalk(
        0x0101,
        (
            '#0010020142V#501F#2P哈啊～\n',
            '早上的空气真是清新……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010020143V#001F#2P看啊，约修亚。\n',
            '从这里能看到咱们家呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020144V#019F#6P真的，能看到屋顶呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020020145V#010F#6P不过，\n',
            '平常你都不想来这里的，\n',
            '今天这是吹的什么风啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020146V我本来以为\n',
            '你不喜欢这个地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020147V#003F#2P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0FE1')
    def lambda_0FE1():
        OP_6E(450, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0FE1)

    OP_20(0x000007D0)
    Sleep(1000)

    ChrSetDirection(0x0101, 180, 300)
    OP_21()
    PlayBGM(83)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010020148V#000F#2P我喜欢这个地方啊。\n',
            '不过，我不会随便来这里的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020149V#500F这是我妈妈……\n',
            '去世的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020150V#014F#6P……哎………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_AD('ED6_DT04/C_VIS006._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(3000)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010020151V',
            (TxtCtl.SetColor, 0xC),
            '１０年前战争的时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0010020152V包围洛连特的帝国军队\n',
            '为了迫使这里的市民投降，\n',
            '而向作为城市象征的钟楼开炮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0010020153V那个时候，\n',
            '爸爸作为王国军的军人参加了战斗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0010020154V我……为了要看看\n',
            '和爸爸战斗的对手是什么样的人，\n',
            '自己一个人登上了这座钟楼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0010020155V但是……就连逃跑的机会都没有，钟楼突然倒塌了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000000C8)
    Sleep(2000)

    OP_AD('ED6_DT04/C_VIS007._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(3000)

    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010020156V不过，当我回过神来的时候，\n',
            '却发现自己毫发无伤……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0010020157V是妈妈……保护了我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0010020158V她用双臂紧紧地抱着我，\n',
            '为我挡住了大量瓦砾的撞击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0010020159V而且，还为哭个不停的我\n',
            '唱起了我最喜欢的摇篮曲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0010020160V然后……然后……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0010020161V当瓦砾被清除之后……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x00000064)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(2000)

    ChrTalk(
        0x0101,
        (
            '#0010020162V#003F#2P………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020163V……战争结束了，\n',
            '这里也被修复成原来的样子。\n',
            '不过自那以后，我就很少来过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020164V因为那是一段非常痛苦的回忆……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020165V#500F一来到这里，\n',
            '心里就不由得有种想要依赖妈妈的感觉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020166V可是，要是依赖了妈妈，\n',
            '就不能像妈妈那样坚强起来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020167V#013F#6P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010020168V#501F#2P不过，没关系吧？\n',
            '至少今天让我依赖一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020169V让我向妈妈祈求，\n',
            '保佑爸爸平安归来也好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020170V让我向妈妈祈求，\n',
            '在天国一直守护着爸爸也好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020171V#015F#6P……当然可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_15DE')
    def lambda_15DE():
        CameraMove(53840, 10300, 44180, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_15DE)

    OP_92(0x0102, 0x0101, 500, 1000, 0x00)
    WaitForThreadExit(0x0000, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020020172V#012F#6P放心吧……\n',
            '父亲一定会平安无事的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020173V有你母亲守护着他，\n',
            '一定会没事的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020174V#003F#2P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020175V#010F#6P就算万一真的出了问题，\n',
            '还有艾丝蒂尔你可以帮助他啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020176V以前母亲救了你，\n',
            '这次该由你去救父亲了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020177V我也会帮忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020178V#003F#2P……约修亚…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020179V#013F#6P你的心情，\n',
            '我虽然不能完全体会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020180V不过像这样呆在你身边……\n',
            '我还是能做到的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020181V#010F如果不介意的话，\n',
            '我的胸膛随时可以借你一用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020182V所以……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020183V#500F#2P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020184V#008F……………噗～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020185V#014F#6P哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    OP_21()
    PlayBGM(1)

    ChrTalk(
        0x0101,
        (
            '#0010020186V#001F#2P啊哈哈哈哈～！\n',
            '约修亚你在耍什么帅啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020187V真是的……\n',
            '这种话你也能这么随便说出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_192C')
    def lambda_192C():
        CameraMove(54620, 10300, 44190, 700)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_192C)

    ChrMoveTo(0x0102, 55250, 10300, 44150, 3000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020020188V#014F#6P哎、哎哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020189V#507F#2P如果是其它女孩的话，\n',
            '肯定会完全误解啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020190V约修亚你啊，\n',
            '将来准是个整日被绯闻缠身的男人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020191V#007F呼～\n',
            '做姐姐的还真是担心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020192V#012F#6P真、真是抱歉，我这么随便。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020193V#013F真是的……\n',
            '人家特意这么关心你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020194V#008F#2P嘿嘿……\n',
            '谢谢你的鼓励啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020195V不管怎么说，有点干劲了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020196V#018F#6P哼，你能这样说，\n',
            '我刚才装帅也是值得了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020197V#017F真是……唉唉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020198V#001F#2P别在意，别在意。\n',
            '我刚才不是说了谢谢嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020199V#006F那么……\n',
            '我们该下去了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020200V雪拉姐肯定在等着了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020201V#010F#6P是啊，我们下去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1C0B')
    def lambda_1C0B():
        CameraMove(54240, 10300, 47980, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1C0B)

    @scena.Lambda('lambda_1C23')
    def lambda_1C23():
        OP_67(0, 6220, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1C23)

    @scena.Lambda('lambda_1C3B')
    def lambda_1C3B():
        OP_6C(324000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_1C3B)

    @scena.Lambda('lambda_1C4B')
    def lambda_1C4B():
        OP_6E(470, 4000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_1C4B)

    CreateThread(0x0102, 0x00, 0x00, func_0A_1DD0)
    Sleep(3000)

    ChrSetFlags(0x0102, 0x0004)
    ChrWalkTo(0x0101, 52498, 10300, 46535, 3000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010020202V#500F……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 135, 400)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010020203V#006F（妈妈，\n',
            '　我终于明白了……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020204V（我以游击士作为自己的目标，\n',
            '　是因为想像妈妈那样\n',
            '　为了保护别人而变得坚强起来……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020205V（所以，请等着我……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020206V（我一定……\n',
            '　我一定会把爸爸平安带回来的！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    CreateThread(0x0101, 0x00, 0x00, func_0B_1E53)
    OP_0D()
    ChrSetFlags(0x0102, 0x0080)
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T0100._SN', 113, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x1DD0
@scena.Code('func_0A_1DD0')
def func_0A_1DD0():
    ChrSetFlags(0x0102, 0x0004)
    ChrWalkTo(0x0102, 52380, 10300, 46390, 2000, 0x00)
    ChrWalkTo(0x0102, 52360, 10300, 47880, 2000, 0x00)
    ChrWalkTo(0x0102, 52850, 10300, 48020, 2000, 0x00)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetDirection(0x0102, 270, 400)
    ChrJumpTo(0x0102, 53700, 9500, 48292, 600, 5000)
    Sleep(500)

    ChrMoveTo(0x0102, 53700, 8300, 48292, 3000, 0x00)
    ChrSetFlags(0x0102, 0x0080)

    Return()

# id: 0x000B offset: 0x1E53
@scena.Code('func_0B_1E53')
def func_0B_1E53():
    ChrSetFlags(0x0101, 0x0004)
    ChrWalkTo(0x0101, 52360, 10300, 47880, 2000, 0x00)
    ChrWalkTo(0x0101, 52850, 10300, 48020, 2000, 0x00)
    ChrSetDirection(0x0101, 270, 400)
    ChrJumpTo(0x0101, 53700, 9500, 48292, 600, 5000)
    Sleep(500)

    ChrMoveTo(0x0101, 53700, 8300, 48292, 3000, 0x00)
    ChrSetFlags(0x0101, 0x0080)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
